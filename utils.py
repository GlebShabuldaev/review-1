def get_key(dic, value):
    """Returns key by value from a dict"""
    for k, v in dic.items():
        if v == value:
            return k
