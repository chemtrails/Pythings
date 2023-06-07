class LoopedList(list):
    def __init__(self, *iterable):
        super().__init__(iterable)

    def __setitem__(self, index, item):
        length = super().__len__()
        index = index % length if index >= length else index
        super().__setitem__(index, item)

    def __getitem__(self, index):
        length = super().__len__()
        index = index % length if index >= length else index
        return super().__getitem__(index)
