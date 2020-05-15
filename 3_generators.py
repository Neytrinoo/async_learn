from time import time


def gen(s):
    for i in s:
        yield i  # передает контроль выполнения, сохраняя момент итерации


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))
        sum = 234 + 234
        print(sum)


g = gen('Dima')
print(next(g))  # D
print(next(g))  # i
print(next(g))  # m
print(next(g))  # a

g = gen_filename()
print(next(g))  # уникальное имя файла
print(next(g))  # 468, уникальное имя файла. next выполняет функцию до следующего yield. yeild'ов может быть несколько
my_generator = (x * x for x in range(3))
for i in my_generator:
    print(i)
for i in my_generator:  # ничего не выведет, т.к. если мы ставим круглые скобки вместо квадратных, то мы создаем генератор, который итерируется лишь единожды
    print(i)
