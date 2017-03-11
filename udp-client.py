import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.connect((target_host, target_port))

client.sendto("AABBCC", (target_host, target_port))

body, address = client.recvfrom(4096)

print body
