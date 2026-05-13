board = [' '] * 9

def show():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

def check(p):

    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == p:
            return True

    return False

for turn in range(9):

    show()

    p = 'X' if turn % 2 == 0 else 'O'

    pos = int(input("Enter position (0-8): "))

    if board[pos] == ' ':
        board[pos] = p

        if check(p):
            show()
            print(p, "Wins")
            break
    else:
        print("Position already filled")

else:
    print("Match Draw")
