from __future__ import annotations
import asyncio
from asyncio.events import AbstractEventLoop
import random


class InfiniteLoopApproach:
    """InfiniteLoopApproach class definition.
    Allow to test asynchronous tasks with an infinite
    browse of event loop approach. This case must be
    used for undetermined runner managing.
    """

    @classmethod
    async def run(cls: InfiniteLoopApproach) -> None:
        """The main method of this script.
        Perform some asynchronous tasks.
        In order, this method is calling 2
        blocking tasks with a set of none blocking
        tasks between us.

        Args:
            cls (InfiniteLoopApproach): The class reference.
        """

        await cls._must_be_blocking_task()
        [
            asyncio.create_task(cls._must_be_daemon_task(_))
            for _ in range(random.randint(1, 5))
        ]
        await cls._must_be_blocking_task()

    @classmethod
    async def _must_be_blocking_task(cls: InfiniteLoopApproach) -> None:
        """The blocking considered method.
        Must be called with the 'await' instruction.

        Args:
            cls (InfiniteLoopApproach): The class reference.
        """

        print('InfiniteLoopApproach._must_be_blocking_task() is running...')
        await asyncio.sleep(2)
        print('InfiniteLoopApproach._must_be_blocking_task() finished.')

    @classmethod
    async def _must_be_daemon_task(cls: InfiniteLoopApproach, n: int) -> None:
        """The unblocking considered method.
        Must be called without the 'await' instruction.

        Args:
            cls (InfiniteLoopApproach): The class reference.
        """

        print(f'InfiniteLoopApproach._must_be_daemon_task({n}) is running...')
        for _ in range(10):
            await asyncio.sleep(0.5)
            print(
                f'InfiniteLoopApproach._must_be_daemon_task({n}) progress: {(_+1)*10}%...'
            )
        print(f'InfiniteLoopApproach._must_be_daemon_task({n}) finished.')


if __name__ == '__main__':
    loop: AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(InfiniteLoopApproach.run())
    loop.run_forever()