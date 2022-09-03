import gc
import time
from copy import deepcopy

from util import reset_color, blue, purple, get_process_memory


class Profiler:
    def __init__(self, fn, *args):
        self.fn = fn
        # allows call to mutate arg and not affect next tests that use same arg
        self.args = deepcopy(args)

    def __enter__(self):
        gc.collect()
        gc.disable()

        self.mem_before = get_process_memory()
        self.start = time.time()

        if self.args:
            return lambda: self.fn(*self.args)

        return self.fn

    def __exit__(self, *exc_info):
        elapsed_time = time.time() - self.start
        mem_after = get_process_memory()

        print("{}{}: {}{} KiB{}, {}{} ms".format(
            purple,
            self.fn.__name__,
            blue,
            (mem_after - self.mem_before) // 2 ** 10,
            purple,
            blue,
            int(elapsed_time * 10 ** 3)),
            reset_color
        )

        gc.enable()
