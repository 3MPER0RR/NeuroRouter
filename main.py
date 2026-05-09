import asyncio

from core.qnn_core import (
    QNN,
    InMemoryStore
)

from core.runtime import Runtime


store = InMemoryStore()

qnn = QNN(
    [7, 16, 8, 1],
    store,
    lr=0.003
)

runtime = Runtime(qnn)


async def main():

    while True:

        text = input(">>> ")

        if text == "exit":
            break

        response = await runtime.process(text)

        print()
        print(response)
        print()


asyncio.run(main())
