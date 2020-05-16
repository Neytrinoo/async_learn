from inspect import getgeneratorstate


def coroutine(func):  # декоратор для инициализации корутин
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g  # в итоге при вызове функции-корутины вернется уже инициализированная корутина

    return inner


class BlaBlaException(Exception):
    pass


def subgen():
    for i in 'oleg':
        yield i


def delegator(g):
    for i in g:  # т.к. генератор - итерируемый объект, то мы можем пройтись по нему в цикле
        yield i


sg = subgen()
g = delegator(sg)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
