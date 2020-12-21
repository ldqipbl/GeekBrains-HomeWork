from socket import socket, AF_INET, SOCK_STREAM
import sys

try:
    ip_add = sys.argv[2]
    port = int(sys.argv[4])
except:
    ip_add = "127.0.0.1"
    port = 7777


def server(ip_add, port):
    SERV_SOCK = socket(AF_INET, SOCK_STREAM)
    SERV_SOCK.bind((ip_add, port))
    SERV_SOCK.listen(5)

    try:
        CLIENT_SOCK, ADDR = SERV_SOCK.accept()

        # принимает сообщение клиента
        NAME_CLIENT = CLIENT_SOCK.recv(4096)
        print(f"Подключеие: \nИмя: {NAME_CLIENT.decode('utf-8')} \nАдрес: {ADDR}")

        # формирует ответ клиенту
        SERV_ENSWER = f"Hello {NAME_CLIENT.decode('utf-8')}"
        # отправляет ответ клиенту
        CLIENT_SOCK.send(SERV_ENSWER.encode('utf-8'))

        CLIENT_SOCK.close()
    finally:
        SERV_SOCK.close()


server(ip_add, port)

