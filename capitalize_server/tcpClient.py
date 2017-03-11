import socket

def main():
    host = "127.0.0.1"
    port = 5000

    client = socket.socket()
    client.connect((host, port))

    message = raw_input("> ")

    while message != 'q':
        client.send(message)
        data = client.recv(1024)
        print "Received from server: %s" % str(data)
        message = raw_input("> ")

    client.close()

main()
