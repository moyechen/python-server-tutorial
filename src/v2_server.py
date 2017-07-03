import socket
import os


def main():
    # create tcp socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # enable reuse address port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind socket to the port
    server_address = ('localhost', 8000)
    s.bind(server_address)
    s.listen(10)
    while 1:
        print('waitting to recevie message from client')
        client, address = s.accept()
        if not os.fork():   # enter child process
            print(client.recv(1024))
            client.close()      # close client socket
            s.close()       # child does not need this
            break
        client.close()      # parent does not need this


if __name__ == '__main__':
    main()
