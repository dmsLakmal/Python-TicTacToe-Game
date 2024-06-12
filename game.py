def board (play):
    for row in play:
        print("|".join(row))
        print("-" * 5 )

playground = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]
              ]

def Player_One(play, a):
    if a == 1:
        playground[0][0]= "X"                        
    elif a == 2:
        playground[0][1]= "X"
    elif a == 3:
        playground[0][2] = "X"
    elif a == 4:
        playground[1][0] = "X"
    elif a == 5:
        playground[1][1] = "X"
    elif a == 6:
        playground[1][2] = "X"
    elif a == 7:
        playground[2][0] = "X"
    elif a == 8:
        playground[2][1] = "X"
    elif a == 9:
        playground[2][2] = "X"

def Player_Two(play, a):        
        if a == 1:
            playground[0][0]= "0"
        elif a == 2:
            playground[0][1]= "0"
        elif a == 3:
            playground[0][2] = "0"
        elif a == 4:
            playground[1][0] = "0"
        elif a == 5:
            playground[1][1] = "0"
        elif a == 6:
            playground[1][2] = "0"
        elif a == 7:
            playground[2][0] = "0"
        elif a == 8:
            playground[2][1] = "0"
        elif a == 9:
            playground[2][2] = "0"

def check_winner(play):
        if play[0][0] == "X" and play[0][1] == "X" and play[0][2] == "X" or play[0][0] == "0" and play[0][1] == "0" and play[0][2] == "0":
            return True
        elif play[1][0] == "X" and play[1][1] == "X" and play[1][2] == "X" or play[1][0] == "0" and play[1][1] == "0" and play[1][2] == "0":
            return True
        elif play[2][0] == "X" and play[2][1] == "X" and play[2][2] == "X" or play[2][0] == "0" and play[2][1] == "0" and play[2][2] == "0":
            return True
        elif play[0][0] == "X" and play[1][0] == "X" and play[2][0] == "X" or play[0][0] == "0" and play[1][0] == "0" and play[2][0] == "0":
            return True
        elif play[0][1] == "X" and play[1][1] == "X" and play[2][1] == "X" or play[0][1] == "0" and play[1][1] == "0" and play[2][1] == "0":
            return True
        elif play[0][2] == "X" and play[1][2] == "X" and play[2][2] == "X" or play[0][2] == "0" and play[1][2] == "0" and play[2][2] == "0":
            return True
        elif play[0][0] == "X" and play[1][1] == "X" and play[2][2] == "X" or play[0][0] == "0" and play[1][1] == "0" and play[2][2] == "0":
            return True
        elif play[0][2] == "X" and play[1][1] == "X" and play[2][0] == "X" or play[0][2] == "0" and play[1][1] == "0" and play[2][0] == "0":
            return True

    
move_count = 0

while True:
    try:
        get_user_input = int(input("Enter Your Position: "))
    except ValueError:
        print("Invalid Input")
        continue

    if get_user_input <= 9:
        if move_count % 2 == 0:
            Player_One(playground, get_user_input)
            board(playground)
            print(playground)
            move_count += 1
            if check_winner(playground):
                print("You Win!")
                break

        elif move_count == 9: 
            print("Match Drawn")
            break

        else:
            Player_Two(playground, get_user_input)
            board(playground)
            print(playground)
            move_count += 1
            if check_winner(playground):
                print("You Win!")
                break
    else:
        print(f"Your Enterd number is out of Range!, Please Enter number range of 1 to 9 or not entering the number")
        continue
        
 