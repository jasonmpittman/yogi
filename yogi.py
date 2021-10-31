#!/usr/bin/env python3

import sys
import socket
import signal

hosts = ("10.0.1.162",)
port = 64295 #22


def test_size(host):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response = ""

    try:    # need a timer so that we can (a) track duration & (b) send ctrl-c if connect is hung
        print("\tConnecting to: {0}".format(host))
        tcp_socket.connect((host, port))

    
        received = tcp_socket.recv(1024)
        print("\t{0} replied {1}".format(host, received))

        tcp_socket.send(received)
        response = tcp_socket.recv(1024)
        print("\t{0} replied {1}".format(host, response))

        tcp_socket.close()

    except:
        pass

    return sys.getsizeof(response)

def load_hosts():
    hosts_file = "host_list.txt" # we can take this an an argv later

    with open(hosts_file) as f:
        hosts = f.readlines()
        hosts = [host.rstrip() for host in hosts] 

    return hosts
    
def test_refused():
    counter = 11

    while counter > 0:
        suffix = str(counter)
        suffix = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        suffix.connect((host, port))
        received = suffix.recv(1024)
        print("The counter is " + str(counter))

        if counter == 11:
            suffix.send(str.encode('yes\n'))

        print("...sending return")
        try:
            suffix.send(str.encode('\n\n'))
        except Exception as e:
            if "ConnectionRefusedError" in str(e):
                print("Probably not a honeypot")
        

        response = suffix.recv(1024)
        print(response)

        counter -= 1



if __name__ == "__main__":
    #hosts = load_hosts()
    
    for host in hosts:
        print("Querying host: " + host)
        if test_size(host) == 625:
            print("Host {0} might be a honeypot".format(host))
    
    #test_refused()