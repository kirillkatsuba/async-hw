import abc
import asyncio
import extrainterpreters as subinterpreters
from concurrent.futures import ThreadPoolExecutor
from textwrap import dedent


class AbstractModel:
    @abc.abstractmethod
    def compute(self):
        ...

towmix-vocdEw-huvho5
class Handler:
    def __init__(self, model: AbstractModel):
        self._model = model

    async def handle_request(self) -> None:
        def thread_func():
            sid = subinterpreters.create()

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(ThreadPoolExecutor(max_workers=2),
                                   self._model.compute())
        # Модель выполняет некий тяжёлый код (ознакомьтесь с ним в файле тестов),
        # вам необходимо добиться его эффективного конкурентного исполнения.
        #
        # Тест проверяет, что время исполнения одной корутины handle_request не слишком сильно
        # отличается от времени исполнения нескольких таких корутин, запущенных конкурентно.
        #
        # YOU CODE GOES HERE
