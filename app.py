import asyncio
import websockets

async def handle_connection(websocket, path):
    # Обработка нового подключения
    print("Новое подключение установлено")

    try:
        while True:
            message = await websocket.recv()
            # Обработка полученного сообщения
            print(f"Получено сообщение: {message}")

            # Отправка ответного сообщения
            response = f"Привет, клиент! Получено сообщение: {message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosedOK:
        # Обработка закрытия соединения
        print("Соединение закрыто")

start_server = websockets.serve(handle_connection, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()