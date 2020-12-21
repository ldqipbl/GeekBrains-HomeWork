from socket import  socket, AF_INET, SOCK_STREAM
import sys

try:
    ip_add = sys.argv[1]
    port = int(sys.argv[2][1:len(sys.argv[2])-1])
except:
    ip_add = '127.0.0.1'
    port = 7777


def client(ip_add, port):
    try:
        CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
        CLIENT_SOCK.connect((ip_add, port))
        
        # сформировать presence-сообщение
        NAME_CLIENT = "Leon"
        # отправить сообщение серверу
        CLIENT_SOCK.send(NAME_CLIENT.encode('utf-8'))

        # получить ответ сервера
        SERV_ENSWER = CLIENT_SOCK.recv(4096)
        # разобрать сообщение сервера
        print(SERV_ENSWER.decode('utf-8'))
        CLIENT_SOCK.close()
    finally:
        CLIENT_SOCK.close()


client(ip_add, port)
