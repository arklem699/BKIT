# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = [str(i) for i in items]
        self.data = set()
        self.index = 0
        self.lst = []
        try:
            self.ignore_case = kwargs["ignore_case"]
        except:
            self.ignore_case = False

    def __next__(self):
        for i in range(0, len(self.items)):
            self.index = i
            el = self.items[self.index]
            if type(el) is str:
                if not self.ignore_case:
                    if el not in self.data:
                        self.data.add(el)
                        return el
                else:
                    if (el.lower() not in self.data) and (el.upper() not in self.data):
                        self.data.add(el)
                        return el
            else:
                if el not in self.data:
                    self.data.add(el)
                    return el

    def __iter__(self):
        return self

    def filling(self):
        el = next(self)
        while el is not None:
            self.lst.append(el)
            el = next(self)
        return self.lst


if __name__ == '__main__':
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(Unique(data).filling())