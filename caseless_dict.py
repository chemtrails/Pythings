class CaselessDict(dict):
    def __init__(self, obj):
        super().__init__(**obj)

    def get(self, key, default=None):
        if (value := super().get(key)) is not None:
            return value
        elif (value := super().get(key.lower())) is not None:
            return value
        elif (value := super().get(key.capitalize())) is not None:
            return value
        elif (value := super().get(key.upper())) is not None:
            return value
        return default
    
    def __getitem__(self, key):
        if (value := super().__getitem__(key)) is not None:
            return value
        elif (value := super().__getitem__(key.lower())) is not None:
            return value
        elif (value := super().__getitem__(key.capitalize())) is not None:
            return value
        elif (value := super().__getitem__(key.upper())) is not None:
            return value
        return super().__getitem__(key)
