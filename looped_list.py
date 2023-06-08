class LoopedList(list):
    def __init__(self, *iterable):
        super().__init__(iterable)

    def __setitem__(self, index, item):
        super().__setitem__(self._convert(index), item)

    def _convert(self, i):
        length = super().__len__()
        return i % length if i >= length else i

    def __getitem__(self, index):
        length = super().__len__()
        if isinstance(index, slice):
            return [
                self.__getitem__(i)
                for i in range(index.start or 0, index.stop or length, index.step or 1)
            ]
        return super().__getitem__(self._convert(index))
