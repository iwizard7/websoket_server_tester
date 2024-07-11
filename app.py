"""
Этот модуль реализует сервер на основе веб-сокетов, который обрабатывает асинхронные подключения.

Он использует библиотеку `websockets` для установления и обработки веб-сокет соединений.
Сервер слушает входящие подключения на порту 8765 и обрабатывает каждое подключение,
используя асинхронную функцию `handle_connection`.
"""

import asyncio
import websockets

async def handle_connection(websocket, _):
    """
    Обрабатывает новое веб-сокет подключение.

    Аргументы:
    websocket -- экземпляр WebSocketServerProtocol, который представляет веб-сокет соединение.
    path -- путь запроса.

    Эта корутинная функция ожидает получения сообщений от клиента, обрабатывает их и отправляет ответ.
    В случае закрытия соединения, корректно обрабатывает исключение ConnectionClosedOK.
    """
    print("Новое подключение установлено")

    try:
        while True:
            message = await websocket.recv()
            # Обработка полученного сообщения
            print(f"Получено сообщение: {message}")

            # Отправка ответного сообщения
            response = ("Привет, клиент! Получено сообщение: "
                        f"{message}")
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosedOK:
        # Обработка закрытия соединения
        print("Соединение закрыто")

start_server = websockets.serve(handle_connection, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
