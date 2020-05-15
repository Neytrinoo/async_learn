def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


# далее идет реализация событийного цикла Round Robin(карусель)
g1 = gen1('Dima')
g2 = gen2(4)
tasks = [g1, g2]
while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
