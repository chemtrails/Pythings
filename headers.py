class Headers(dict):
    def __init__(self, obj):
        super().__init__()
        super().update(obj)

    def get(self, key: str, default=None):
        key = key.lower()
        for _key in self.keys():
            if _key.lower() == key or (isinstance(_key, bytes) and _key.decode().lower() == key):
                res = super().__getitem__(_key)
                if isinstance(res, bytes):
                    return res.decode()
                return res
        return default

    def __getitem__(self, key: str):
        key = key.lower()
        for _key in self.keys():
            if _key.lower() == key or (isinstance(_key, bytes) and _key.decode().lower() == key):
                res = super().__getitem__(_key)
                if isinstance(res, bytes):
                    return res.decode()
                return res
        raise KeyError(key)
