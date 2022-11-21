def field(items, *args):
    assert len(args) > 0
    if len(args) > 1:
        for el in items:
            dct = {}
            for keys, val in el.items():
                for arg in args:
                    if keys == arg:
                        dct[keys] = val
            yield dct
    else:
        for el in items:
            for keys in el:
                for arg in args:
                    if keys == arg:
                        yield el[keys]


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))