from patterns_lab.caching.cache_decorator import simple_cache


calls = 0


@simple_cache
def square(x):
    global calls
    calls += 1
    return x * x


def test_cache():
    square(2)
    square(2)
    assert calls == 1