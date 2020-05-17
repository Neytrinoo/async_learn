import asyncio


async def step1():
    a = await asyncio.get_event_loop().run_in_executor(None, input)
    print(a)


async def step2():
    print(3 ** 1234567)


async def main():
    task1 = asyncio.create_task(step1())
    task2 = asyncio.create_task(step2())
    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
