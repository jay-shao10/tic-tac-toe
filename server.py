import socket
import random
from _thread import *
host = '127.0.0.1'
port = 1233
ThreadCount = 0

def client_handler(connection):
    data = [" "]*10
    sample = ["1","2","3","4","5","6","7","8","9"]
    
    while True:
        num = connection.recv(2048)
        num2 = num.decode('utf-8')
        print(num2)
        data[int(num2)] = "x"
        if num2 in sample:
            sample.remove(num2)
        if check(data):
            break
        cmd = random.choice(sample)
        print(cmd)
        data[int(cmd)] = "o"
        reply =cmd
        connection.sendall(reply.encode('utf-8'))  # 不需要對已經編碼的字節對象再次進行編碼
        if cmd in sample:
            sample.remove(cmd)
        if check(data):
            break
    connection.close()


def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print(f'Connected to: {address[0]}:{str(address[1])}')
    start_new_thread(client_handler, (Client, )) 
def check(data):
    if data[1] == data[2] and data[1] == data[3] and data[1]=="x":
        print("Player1 win!!!")
        return True
    if data[4] == data[5] and data[4] == data[6] and data[4]=="x":
        print("Player1 win!!!")
        return True
    if data[7] == data[8] and data[7] == data[9] and data[7]=="x":
        print("Player1 win!!!")
        return True
    if data[1] == data[4] and data[1] == data[7] and data[1]=="x":
        print("Player1 win!!!")
        return True
    if data[2] == data[5] and data[2] == data[8] and data[2]=="x":
        print("Player1 win!!!")
        return True
    if data[3] == data[6] and data[3] == data[9] and data[3]=="x":
        print("Player1 win!!!")
        return True
    if data[1] == data[5] and data[1] == data[9] and data[1]=="x":
        print("Player1 win!!!")
        return True
    if data[3] == data[5] and data[3] == data[7] and data[3]=="x":
        print("Player1 win!!!")
        return True
    

    if data[1] == data[2] and data[1] == data[3] and data[1]=="o":
        print("Player2 win!!!")
        return True
    if data[4] == data[5] and data[4] == data[6] and data[4]=="o":
        print("Player2 win!!!")
        return True
    if data[7] == data[8] and data[7] == data[9] and data[7]=="o":
        print("Player2 win!!!")
        return True
    if data[1] == data[4] and data[1] == data[7] and data[1]=="o":
        print("Player2 win!!!")
        return True
    if data[2] == data[5] and data[2] == data[8] and data[2]=="o":
        print("Player2 win!!!")
        return True
    if data[3] == data[6] and data[3] == data[9] and data[3]=="o":
        print("Player2 win!!!")
        return True
    if data[1] == data[5] and data[1] == data[9] and data[1]=="o":
        print("Player2 win!!!")
        return True
    if data[3] == data[5] and data[3] == data[7] and data[3]=="o":
        print("Player2 win!!!")
        return True
    return False
def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)
start_server(host, port)
        







