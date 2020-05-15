import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)  # регистрируем серверный сокет. становится виден только когда
    # мы пытаемся к нему подключиться


def accept_connection(server_socket):
    print('before accept()')
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)  # регистрируем клиентский сокет. становится виден только когда
    # мы отправляем сообщение


def send_message(client_socket):
    print('Before .recv()')
    request = client_socket.recv(4096)
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)  # снимаем клиентский сокет с регистрации перед закрытием
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()  # (key, events) key - объект SelectorKey. у него есть поля fileobj, events и data
        for key, _ in events:
            callback = key.data  # получаем функцию
            callback(key.fileobj)  # вызываем полученную функцию с файлом. т.е. если у нас в fileobj находится клиентский сокет, то вызывем функцию
            # sens_message(client_socket)


if __name__ == '__main__':
    server()
    event_loop()
