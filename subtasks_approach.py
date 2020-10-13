from __future__ import annotations
import asyncio
from asyncio.events import AbstractEventLoop
import random
from typing import Coroutine, List


class SubTasksApproach:
    """SubTasksApproach class definition.
    Allow to test asynchronous tasks with a complete
    browse of event loop. This case must be used for
    determined runner managing.
    """

    @classmethod
    async def run(cls: SubTasksApproach) -> None:
        """The main method of this script.
        Perform some asynchronous tasks.
        In order, this method is calling 2
        blocking tasks with a set of none blocking
        tasks between us.

        Args:
            cls (SubTasksApproach): The class reference.
        """

        await cls._must_be_blocking_task()
        tasks: List[Coroutine] = [
            asyncio.create_task(cls._must_be_daemon_task(_))
            for _ in range(random.randint(1, 5))
        ]
        await cls._must_be_blocking_task()
        await asyncio.gather(*tasks)

    @classmethod
    async def _must_be_blocking_task(cls: SubTasksApproach) -> None:
        """The blocking considered method.
        Must be called with the 'await' instruction.

        Args:
            cls (SubTasksApproach): The class reference.
        """

        print('SubTasksApproach._must_be_blocking_task() is running...')
        await asyncio.sleep(2)
        print('SubTasksApproach._must_be_blocking_task() finished.')

    @classmethod
    async def _must_be_daemon_task(cls: SubTasksApproach, n: int) -> None:
        """The unblocking considered method.
        Must be called without the 'await' instruction.

        Args:
            cls (SubTasksApproach): The class reference.
        """

        print(f'SubTasksApproach._must_be_daemon_task({n}) is running...')
        for _ in range(10):
            await asyncio.sleep(0.5)
            print(
                f'SubTasksApproach._must_be_daemon_task({n}) progress: {(_+1)*10}%...'
            )
        print(f'SubTasksApproach._must_be_daemon_task({n}) finished.')


if __name__ == '__main__':
    asyncio.run(SubTasksApproach.run())