def fibonacci(n):
    if n <= 0 or type(n) not in [int]:
        raise ValueError

    num1, num2 = 0, 1
    for _ in range(n):
        num1, num2 = num2, num2 + num1
        yield num1


if __name__ == '__main__':
    print(*fibonacci(5))