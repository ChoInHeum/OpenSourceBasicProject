def print_board(board):
    for r in range(3):
        print(" " + " | ".join(board[r]))
        if r != 2:
            print("---|---|---")

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

board = [[' ' for _ in range(3)] for _ in range(3)]

while True:
    print_board(board)
    
    try:
        x, y = map(int, input("다음 수의 좌표를 입력하세요 (x y): ").split())
        if x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != ' ':
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue
    except ValueError:
        print("숫자 두 개를 입력하세요.")
        continue

    board[x][y] = 'X'

    if check_winner(board, 'X'):
        print_board(board)
        print("당신이 이겼습니다!")
        break

    if is_full(board):
        print_board(board)
        print("무승부입니다!")
        break

    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                done = True
                break
        if done:
            break

    if check_winner(board, 'O'):
        print_board(board)
        print("컴퓨터가 이겼습니다!")
        break

    if is_full(board):
        print_board(board)
        print("무승부입니다!")
        break