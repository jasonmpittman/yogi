#!/usr/bin/env python3

import sys
import socket

host = '10.0.1.162'
port = 64295


def test_size():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((host, port))
    received = tcp_socket.recv(1024)
    
    tcp_socket.send(received)
    response = tcp_socket.recv(1024)
    
    return sys.getsizeof(response)

    tcp_socket.close()

def test_refused():
    counter = 6

    while counter > 0:
        suffix = str(counter)
        suffix = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        suffix.connect((host, port))
        received = suffix.recv(1024)
        print("...sending return")

        suffix.send(str.encode('\n'))
        response = suffix.recv(1024)
        print(response)

        counter -= 1



if __name__ == "__main__":
    if test_size() == 625:
        print("It might be a honeypot")
        #test_refused()