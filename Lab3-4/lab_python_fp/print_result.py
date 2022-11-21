def print_result(func):
    def wrapper(*args):
        print(func.__name__)
        res = func(*args)
        if type(res) == dict:
            dct = res
            for i in dct:
                print(i, '=', dct[i])
        elif type(res) == list:
            lst = res
            for i in lst:
                print(i)
        else:
            if func.__name__ != 'print':
                print(res)
            else:
                res
        return res
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()