from time import time, sleep
from contextlib import contextmanager

class cm_timer_1:

    def __init__(self):
        self.start = 0
        self.finish = 0

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish = time()
        print("Время работы: ", self.finish - self.start)


@contextmanager
def cm_timer_2():
    start = time()
    yield None
    finish = time()
    print("Время работы: ", finish - start)


if __name__ == '__main__':
    with cm_timer_1():
        sleep(2)
    with cm_timer_2():
        sleep(2)