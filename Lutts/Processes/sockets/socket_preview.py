from socket import socket, AF_INET, SOCK_STREAM     #API сокетов

port = 50008                #номер порта, идентифицируюищй сокет
host = 'localhost'          #сервер и клиент выполняются на локальном компьютере

def server():
    sock = socket(AF_INET, SOCK_STREAM)         #IP-адрес TCP-соединения
    sock.bind(('', port))                       #подключить к порту на этой машине
    sock.listen(5)                              #до 5 ожидающих клиентов

    while True:
        conn, addr = sock.accept()              #ждать соединения с клиентом
        data = conn.recv(1024)                  #прочитать байты данных от клиента
        reply = 'server got: [%s]' % data       #conn - новый подключенный сокет
        conn.send(reply.encode())               #отправить байты данных клиенту


def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))                #подключить сокет к порту
    sock.send(name.encode())                  #отправить байты данных серверу
    reply = sock.recv(1024)                   #принять байты данных от сервера
    sock.close()                              #до 1024 байтов в сообщении
    print('client got: [%s]' % reply)


if __name__ == '__main__':
    from Lib.threading import Thread
    sthread = Thread(target=server)
    sthread.daemon = True                     #не ждать завершения потока сервера
    sthread.start()                           #ждать завершения дочерних потоков
    for i in range(5):
        Thread(target=client,args=('client%s' % i)).start()

