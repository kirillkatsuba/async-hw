import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    result = await asyncio.gather(*coros)
    result = sorted(result)
    answer = ''
    for ticket in result:
        answer += ticket.key
    return answer
