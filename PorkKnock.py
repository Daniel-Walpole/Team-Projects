import socket
import itertools
import sys

destination = "192.168.56.203"
ports = [5260,12345,36031]

def main():
    print ("[+] Sequence is %s" % ports)
    for port in ports:
        print ("[+] Knocking on port %s:%s" % (destination,port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect_ex((destination, port))
        sock.close()
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while(True):
        connection.connect_ex((destination,42020))
        connection.settimeout(100)
    connection.close()

if __name__ == '__main__':
    main()
