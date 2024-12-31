import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    async with asyncio.timeout(max_execution_time):
        try:
            await coro
        except asyncio.CancelledError:
            print('I am alive!')


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    async with asyncio.timeout(max_execution_time):
        try:
            await asyncio.gather(*coros)
        except asyncio.CancelledError:
            print('I am alive!')
