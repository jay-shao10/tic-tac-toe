def print_board(data):
    print(f"{data[1]}|{data[2]}|{data[3]}")
    print("-----")
    print(f"{data[4]}|{data[5]}|{data[6]}")
    print("-----")
    print(f"{data[7]}|{data[8]}|{data[9]}")
    print("==========")
    print("==========")

def check(data):
    if data[1] == data[2] and data[1] == data[3] and data[1]=="x":
        print("you win!!!")
        return True
    if data[4] == data[5] and data[4] == data[6] and data[4]=="x":
        print("you win!!!")
        return True
    if data[7] == data[8] and data[7] == data[9] and data[7]=="x":
        print("you win!!!")
        return True
    if data[1] == data[4] and data[1] == data[7] and data[1]=="x":
        print("you win!!!")
        return True
    if data[2] == data[5] and data[2] == data[8] and data[2]=="x":
        print("you win!!!")
        return True
    if data[3] == data[6] and data[3] == data[9] and data[3]=="x":
        print("you win!!!")
        return True
    if data[1] == data[5] and data[1] == data[9] and data[1]=="x":
        print("you win!!!")
        return True
    if data[3] == data[5] and data[3] == data[7] and data[3]=="x":
        print("you win!!!")
        return True
    

    if data[1] == data[2] and data[1] == data[3] and data[1]=="o":
        print("computer win!!!")
        return True
    if data[4] == data[5] and data[4] == data[6] and data[4]=="o":
        print("computer win!!!")
        return True
    if data[7] == data[8] and data[7] == data[9] and data[7]=="o":
        print("computer win!!!")
        return True
    if data[1] == data[4] and data[1] == data[7] and data[1]=="o":
        print("computer win!!!")
        return True
    if data[2] == data[5] and data[2] == data[8] and data[2]=="o":
        print("computer win!!!")
        return True
    if data[3] == data[6] and data[3] == data[9] and data[3]=="o":
        print("computer win!!!")
        return True
    if data[1] == data[5] and data[1] == data[9] and data[1]=="o":
        print("computer win!!!")
        return True
    if data[3] == data[5] and data[3] == data[7] and data[3]=="o":
        print("computer win!!!")
        return True
    if data[1] != " " and  data[2] != " " and data[3] != " " and data[4] != " " and data[5] != " " and data[6] != " " and data[7] != " " and data[8] != " " and data[9] != " " :
        print("tie!!!")
        return True
    return False

example = ["0","1","2","3","4","5","6","7","8","9"]
print_board(example)
data = [" "]*10
import socket
HOST='127.0.0.1'
PORT=1233

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    cmd = input("請輸入數字：")
    s.send(cmd.encode('utf-8'))
    data[int(cmd)] = "x"
    print_board(data)
    if check(data):
        break

    num = s.recv(1024)
    if not num:
        # 處理未收到數據的情況
        print("未收到來自server的數據")
        continue  # 或者任何其他適當的操作
    num = num.decode('utf-8')
    print("server數據:", num)
    try:
        num = int(num)
    except ValueError:
        print("從server收到的數據無效:", num)
        continue  # 或者任何其他適當的操作

    data[num] = "o"
    print_board(data)
    if check(data):
        break


    
