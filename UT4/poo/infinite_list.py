class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.args = args
        self.fill_value = fill_value
        self.items = [arg for arg in args]

    def __getitem__(self, index: int):
        while len(self.items) < index:
            self.items.append(self.fill_value)
            if len(self.items) >= index:
                return self.items[index]

    def __len__(self):
        if not self.items:
            self.items.append(self.fill_value)
        return len(self.items)

    def __setitem__(self, index: int, item) -> None:
        while len(self.items) < index:
            self.items.append(self.fill_value)
            if len(self.items) >= index:
                self.items[index] = item
                return self.items

    def __str__(self):
        bocadillo_de_pollo = ','.join(str(self.items))
        return f'{bocadillo_de_pollo}'
