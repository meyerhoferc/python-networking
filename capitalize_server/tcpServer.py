import socket

def main():
    host = '127.0.0.1'
    port = 5000

    server = socket.socket()
    server.bind((host, port))

    # listen for 1 connection at a time
    server.listen(1)
    
    # accept the new connection
    connection, address = server.accept()
    print "Connection from : %s received" % str(address)

    while True:
        # buffer max is 1024 bytes
        data = connection.recv(1024)
        if not data: break

        print "from connection user: %s" % str(data)
        data = str(data).upper()
        print "sending: %s" % str(data)
        connection.send(data)
    connection.close()

main()
