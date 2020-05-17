import asyncio
import socket


def create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    return server_socket


async def get_message(client_socket):
    request = client_socket.recv(4096)
    return request


async def get_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    print(await asyncio.create_task(get_message(client_socket)))


async def main():
    server_socket = create_server_socket()
    while True:
        await asyncio.create_task(get_connection(server_socket))


if __name__ == '__main__':
    asyncio.run(main())
