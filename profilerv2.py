# TODO look into divergent behavior depending on clone=True or False
import gc
import time
from copy import deepcopy
from dataclasses import dataclass

from util import red, get_process_memory, yellow, purple, reset_color, blue, light_green, orange, bright_blue, \
    bright_red


@dataclass
class Metrics:
    space_usage: int = 0
    time_usage: int = 0


@dataclass
class Identifier:
    """
    Only used to generate random ID for a given instance.
    """
    pass


class MetricsCollector:
    def __init__(self, metrics: Metrics):
        """
        :param metrics: Object to be filled by MetricCollector on exit. Will contain 'space_usage' and 'time_usage'
        """
        self.metrics = metrics

    def __enter__(self):
        gc.collect()
        gc.disable()

        self.mem_before = get_process_memory()
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.metrics.space_usage = (get_process_memory() - self.mem_before)
        self.metrics.time_usage = (time.time() - self.start)

        gc.enable()


class MetricsPrinter:
    @staticmethod
    def get_color_from_factor(factor):
        if factor < 1.1:
            return light_green
        if factor < 1.6:
            return blue
        if factor < 2.1:
            return yellow
        if factor < 4.1:
            return orange
        return red

    def __init__(self, var, n_ct, ncolor, prev_metrics):
        self.metrics = Metrics()
        self.ncolor = ncolor
        self.var = var
        self.n_ct = n_ct
        self.prev_metrics = prev_metrics

    def __enter__(self):
        """
        :return: a Metrics object that must be passed to the MetricsCollector to fill
        """
        return self.metrics

    def __exit__(self, exc_type, exc_val, exc_tb):
        space_factor, time_factor = 0, 0
        space_factor_str, time_factor_str = '', ''

        if self.prev_metrics.space_usage:
            space_factor = round(self.metrics.space_usage / self.prev_metrics.space_usage, 2)
            space_factor_str = f'({space_factor}x)'

        if self.prev_metrics.time_usage:
            time_factor = round(self.metrics.time_usage / self.prev_metrics.time_usage, 2)
            time_factor_str = f'({time_factor}x)'

        self.prev_metrics.space_usage, self.prev_metrics.time_usage = self.metrics.space_usage, self.metrics.time_usage

        print("{}{}: {: <8}{}{: >12} KiB  {}{: <8}{}{: >10} ms  {}{: <8}{}".format(
            self.ncolor,
            self.var,
            self.n_ct,
            reset_color,
            self.metrics.space_usage,
            self.get_color_from_factor(space_factor),
            space_factor_str,
            reset_color,
            self.metrics.time_usage,
            self.get_color_from_factor(time_factor),
            time_factor_str,
            reset_color
        ))


class ProfilerV2:
    color = bright_blue

    @classmethod
    def get_color(cls):
        # Toggle color for new time
        cls.color = bright_blue if cls.color == bright_red else bright_red
        return cls.color

    def __init__(self, fn, var, start, reps=1, mapper=(lambda x: x), clone=True):
        """
        Profiler takes configurations, including the function you want to profile,
        and returns that function wrapped in a way such that the second element of
        return, a token, can be used to identify which argument of the profiled
        function to vary within the tests.

        :param fn: Function to profile
        :param var: Variable name to print (i.e. "n")
        :param start: The seed value to use
        :param reps: Number of times to repeat for each run
        :param mapper: Function that maps each value to the desired value to pass to fn
        :param clone: Bool for whether to deep copy argument before tests. Set to false if arg is too deeply nested.
        """
        self.fn = fn
        self.var = var
        self.n_list = map(lambda x: (x, mapper(x)), map(lambda x: start * 2 ** x, range(4)))
        self.ntoken = Identifier()
        self.reps = reps
        self.clone = deepcopy if clone else lambda x: x

    def __enter__(self):
        def wrapper(*args, **kwargs):
            ncolor = self.__class__.get_color()
            print(f'{purple}{self.fn.__name__}{reset_color}')
            prev_metrics = Metrics()

            for n_ct, n_arg in self.n_list:
                with MetricsPrinter(self.var, n_ct, ncolor, prev_metrics) as curr_metrics:
                    argslist = [
                        tuple(self.clone(n_arg if arg is self.ntoken else arg) for arg in args) for _ in
                        range(self.reps)
                    ]
                    kwargslist = [
                        dict(self.clone((k, n_arg) if v is self.ntoken else (k, v)) for k, v in kwargs.items()) for _ in
                        range(self.reps)
                    ]

                    with MetricsCollector(curr_metrics):
                        for i in range(self.reps):
                            self.fn(*(argslist[i]), **(kwargslist[i]))

            # Beware, no return provided for decorated function

        return wrapper, self.ntoken

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
