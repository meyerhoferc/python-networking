import socket
import time

host = "127.0.0.1"
port = 5000

clients = []

# set up a UDP connection
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

# does not block any from the data stream
server.setblocking(0)

quitting = False
print "Server Started"

while not quitting:
    try:
        data, address = server.recvfrom(1024)
        if "Quit" in str(data): quitting = True
        if address not in clients: clients.append(address)
        print time.ctime(time.time()) + str(address) + ": :" + str(data)

        for client in clients:
            server.sendto(data, client)

    except:
        pass
        
server.close()
