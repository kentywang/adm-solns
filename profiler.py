import gc
import time
import os
import psutil
import tracemalloc

reset_color = '\033[0m'
blue = '\033[0;96m'
purple = '\033[0;95m'

def get_process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()

    return mem_info.rss


# tracemalloc disabled for now because I don't understand how it works
# Also the other memory profiling method works fine for now, I think
def profile(func):
    def wrapper(*args, **kwargs):
        gc.collect()
        gc.disable()

        # tracemalloc.start(10)
        # time1 = tracemalloc.take_snapshot()

        mem_before = get_process_memory()
        start = time.time()

        result = func(*args, **kwargs)

        elapsed_time = time.time() - start
        mem_after = get_process_memory()

        # time2 = tracemalloc.take_snapshot()

        print("{}{}: {}{} KiB{}, {}{} ms".format(
            purple,
            func.__name__,
            blue,
            (mem_after - mem_before) // 2 ** 10,
            purple,
            blue,
            int(elapsed_time * 10 ** 3)),
            reset_color
        )

        # stats = time2.compare_to(time1, 'lineno')  # Compare snapshots
        # for stat in stats[:3]:
        #     print(stat)

        return result

    return wrapper
