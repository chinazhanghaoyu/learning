import socket,threading,time
def delClient(sock,addr):
    print('Accept new connection from %s:%s...'% addr)
    sock.send(b'hello,I am server!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == (exit):
            break
        print('-->>%s!' % data.decode('utf-8'))
        sock.sent(('Lop_msg: %s ! ' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.'% addr)
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('`127.0.0.1'))
