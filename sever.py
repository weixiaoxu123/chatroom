import socket
import sys
import struct

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
addrall =[]
#unpacker = struct.Struct('I 50s 100s')
while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    try:
        print(sys.stderr, 'connection from', server_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data,addr = sock.recvfrom(1000)
            if addr not in addrall:
                addrall.append(addr)
                print(addr)
            print(sys.stderr, 'received "%s "' % data.decode('utf-8'))
            print(addrall)
            if data:
                print(sys.stderr, 'sending data back to the client')
                for addr_to in addrall:
                    sock.sendto(data,addr_to)
            else:
                print(sys.stderr, 'no data from', addr)
                break
    finally:
        # Clean up the connection
        sock.close()