import json
import sys
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.unique import Unique
from lab_python_fp.gen_random import gen_random
from lab_python_fp.field import field

path = 'data_light.json'
with open(path, "rb") as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(Unique(field(data, "job-name")).filling()))


@print_result
def f2(arg):
    return list(filter(lambda s: s.startswith("Программист") or s.startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda s: s + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list(zip(arg, ['зарплата ' + str(i) + ' руб.' for i in gen_random(len(arg), 100000, 200000)]))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))