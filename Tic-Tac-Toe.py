


board=[]
player_token = ""


def main():
    counter = 0
    winner  = False
    while not winner:
        draw_board(board)
        display_board(board)
        if counter % 2==0:
            take_input("X")
        else:
            take_input("O")
        counter+=1
        if counter > 4:
            temp = check_win(board)
            if temp:
                display_board(board)
                print (temp, "won!")
                winner = True
                break
        if counter == 9:
            display_board(board)
            print ("Friendship won!")
            break
    

    #take_input(player_token)

def draw_board(board):
    for square in range(10):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print (board[0], "|", board[1], "|", board[2] )
    print('----------')
    print (board[3], "|", board[4], "|", board[5] )
    print('----------')
    print(board[6], "|", board[7], "|", board[8] )
    print()

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Where to place " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Are you sure your input is a number?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("This field is already busy")
        else:
            print ("Incorrect input! Use number in range 1-9")


def check_win(board):
    winner_coordinates = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in winner_coordinates:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False




if __name__ == '__main__':
    main()

