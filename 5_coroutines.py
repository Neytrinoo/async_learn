from inspect import getgeneratorstate


def coroutine(func):  # декоратор для инициализации корутин
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g  # в итоге при вызове функции-корутины вернется уже инициализированная корутина

    return inner


@coroutine
def subgen():
    x = 'Ready to accept message'
    message = yield x  # в данном случае можно представлять себе yield как двустороннюю форточку. Она одновременно и отдает нам x, и принимает внешние значения
    print('Subgen received:', message)


g = subgen()
print(getgeneratorstate(g))  # GEN_CREATED
# print(g.send(None))  # x (Ready to accept message). Функция возвращает нам x и приостанавливается до следующего вызова
print(getgeneratorstate(g))  # GEN_SUSPENDED
try:
    g.send('ok')  # передаем в yield строку 'ok'
except StopIteration:
    pass


@coroutine
def average():
    count = 0
    summ = 0
    average = None
    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average


print('--------------------------')
g = average()
# print(g.send(None))  # необходимая инициализация корутины(после декоратора больше не необходимая
print(g.send(4))
print(g.send(10))
try:
    g.throw(StopIteration)  # вызываем принудительно StopIteration
except StopIteration as e:
    print('Average', e)
