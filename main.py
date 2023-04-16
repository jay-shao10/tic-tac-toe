def print_board(data):
    print(f"{data[1]}|{data[2]}|{data[3]}")
    print("-----")
    print(f"{data[4]}|{data[5]}|{data[6]}")
    print("-----")
    print(f"{data[7]}|{data[8]}|{data[9]}")
    print("==========")
    print("==========")

def print_winner_msg(is_player_one):
    if is_player_one == 1:
        print("Player1 win!!!")
    else:
        print("Player2 win!!!")


def check(data,is_player_one):
    if data[1] == data[2] and data[1] == data[3] and data[1]!=" ":
        print_winner_msg(is_player_one)
        return True
    if data[4] == data[5] and data[4] == data[6] and data[4]!=" ":
        print_winner_msg(is_player_one)
        return True
    if data[7] == data[8] and data[7] == data[9] and data[7]!=" ":
        print_winner_msg(is_player_one)
        return True
    if data[1] == data[4] and data[1] == data[7] and data[1]!=" ":
        print_winner_msg(is_player_one)
        return True
    if data[2] == data[5] and data[2] == data[8] and data[2]!=" ":
        print_winner_msg(is_player_one)
        return True
    if data[3] == data[6] and data[3] == data[9] and data[3]!=" ":
        print_winner_msg(is_player_one)
        return True
    if data[1] == data[5] and data[1] == data[9] and data[1]!=" ":
        print_winner_msg(is_player_one)
        return True
    if data[3] == data[5] and data[3] == data[7] and data[3]!=" ":
        print_winner_msg(is_player_one)
        return True
    return False



example = ["0","1","2","3","4","5","6","7","8","9"]
print_board(example)

data = [" "]*10
# player one is "x", player two is "o"
is_player_one = 1

while True:
    x = int(input("input the place you want to fill in!"))
    if is_player_one == 1:
        data[x] = "x"
    else:
        data[x] = "o"
    print_board(data)
    if check(data,is_player_one):
        break
    is_player_one *= -1
    
