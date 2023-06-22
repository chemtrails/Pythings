def get_first(key: str, obj):
    if isinstance(obj, dict):
        for _key, value in obj.items():
            if _key == key:
                return value
            if (res := get_first(key, value)) is not None:
                return res
        return None
    elif isinstance(obj, list):
        for item in obj:
            if (res := get_first(key, item)) is not None:
                return res
        return None
    return None
