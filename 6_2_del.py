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
    while True:
        try:
            message = yield
        except StopIteration:
            print('Ku-ku!!!')
            break
        else:
            print('............')
    return 'Returned from subgen()'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)  # взыываем исключение BlaBlaException у подгенератора subgen
    result = yield from g  # вместо того, что написано выше. в result сохранится то, что возвращает подгенератор в return'е.
    # также конструкция yield from generator_name автоматически инициализирует generator_name, поэтому не нужно декорировать его написанной ранее функцией-декоратором coroutine
    # по другому можно понять, что yield from просто итерирует подгенератор.
    print(result)


sg = subgen()
g = delegator(sg)
g.send('ok')
g.throw(StopIteration)
