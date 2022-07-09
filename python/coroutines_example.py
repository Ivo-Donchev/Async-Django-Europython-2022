from sys import argv
import asyncio
import threading


async def func(coroutine_idx):
    print(f'Coroutine {coroutine_idx} started')
    await asyncio.sleep(1)
    print(f'Coroutine {coroutine_idx} finished')


async def main():
    await asyncio.gather(
        *[
            func(i)
            for i in range(1, 11)
        ]
    )


if __name__ == '__main__':
    asyncio.run(main())
