import asyncio
import websockets



async def client():
    async with websockets.connect('ws://localhost:8765') as ws:
        message = "Hello World"
        print(f"Отправка {message}")
        await ws.send(message)
        response = await ws.recv()
        print(f"Ответ от сервера {response}")
        for _ in range(5):
            response = await ws.recv()
            print(f"Ответ от сервера {response}")

asyncio.run(client())