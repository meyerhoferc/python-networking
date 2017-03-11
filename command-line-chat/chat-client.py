import socket
import threading
import time

tlock = threading.Lock()
shutdown = False

def receiving(name, socket):
    while not shutdown:
        try:
            tlock.acquire()
            while True:
                data, address = socket.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tlock.release()

host = "127.0.0.1"
port = 0
server = ("127.0.0.1", 5000)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((host, port))
client.setblocking(0)

receiving_thread = threading.Thread(target=receiving, args=("RecvThread", client))
receiving_thread.start()

alias = raw_input("Name: ")
message = raw_input(alias + " #:> ")

while message != "q":
    if message != '':
        client.sendto(alias + "#:> " + message, server)
        tlock.acquire()
        message = raw_input(alias + "#:> ")
        tlock.release()
        time.sleep(0.2)

shutdown = True
receiving_thread.join()
client.close()
