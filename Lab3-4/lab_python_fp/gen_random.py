from random import randint

lst = []


def gen_random(num_count, begin, end):
    for i in range(0, num_count):
        lst.append(randint(begin, end))
    numbers = map(str, lst)
    print(', '.join(numbers))
    return lst


if __name__ == '__main__':
    gen_random(5, 0, 10)