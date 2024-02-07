from collections import OrderedDict

cache = OrderedDict()
CACHE_MAX_SIZE = 700


def get_from_cache(key):
    if key in cache:
        value = cache.pop(key)
        cache[key] = value
        return value
    return None


def put_in_cache(key, value):
    if len(cache) >= CACHE_MAX_SIZE:
        cache.popitem(last=False)
    cache[key] = value