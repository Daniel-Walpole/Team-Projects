import socket
import itertools
import sys

destination = "10.16.189.81"
ports = [5260,12345,36031,42020]

def main():
    print ("[+] Sequence is %s" % ports)
    for port in ports:
        print ("[+] Knocking on port %s:%s" % (destination,port))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((destination, port))
            s.sendall(b'Y')
            s.close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
        print ("[+] Knocking on port %s:%s" % (destination,42069))
        f.connect_ex((destination, 42069))
        f.sendall(b'12345678901234')
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = f.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks) 
        f.close()

if __name__ == '__main__':
    main()
