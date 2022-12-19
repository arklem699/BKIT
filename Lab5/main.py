import sys
import math


def get_coef(index, prompt):
    flag = 0
    while flag == 0:
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
        try:
            coef = float(coef_str)
            flag = 1
        except ValueError:
            print('Вы ввели не число! Попробуйте снова')
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if a == 0.0 and b != 0.0:
        if -c / b >= 0.0:
            root = math.sqrt(-c/b)
            if root != 0.0:
                result.append(-root)
                result.append(root)
            else:
                result.append(abs(root))
    elif a == 0.0 and b == 0.0:
        if c == 0.0:
            print('Бесконечное множество корней')
            exit(1)
        else:
            print('Нет корней')
            exit(1)
    elif D == 0.0:
        if -b / (2.0 * a) >= 0.0:
            root = math.sqrt(-b / (2.0 * a))
            if root != 0.0:
                result.append(root)
                result.append(-root)
            else:
                result.append(abs(root))
    elif D > 0.0:
        if (-b + math.sqrt(D)) / (2.0 * a) >= 0.0:
            root1 = math.sqrt((-b + math.sqrt(D)) / (2.0 * a))
            if root1 != 0.0:
                result.append(root1)
                result.append(-root1)
            else:
                result.append(abs(root1))
        if (-b - math.sqrt(D)) / (2.0 * a) >= 0.0:
            root2 = math.sqrt((-b - math.sqrt(D)) / (2.0 * a))
            if root2 != 0.0:
                result.append(root2)
                result.append(-root2)
            else:
                result.append(abs(root2))
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    if len(roots) == 0:
        print('Нет корней')
    elif len(roots) == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len(roots) == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len(roots) == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len(roots) == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


if __name__ == "__main__":
    main()