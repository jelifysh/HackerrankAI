# Head ends here

def next_move(posr, posc, board):
    if (board[posr][posc] == 'd'):
        print("CLEAN");
    else:
        min_dist = -1
        dr = posr
        dc = posc
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'd':
                    dist = (row - posr) ** 2 + (col - posc) ** 2
                    if min_dist == -1 or dist < min_dist:
                        min_dist = dist
                        dr = row
                        dc = col
        
        if dr > posr:
            print("DOWN")
        elif dr < posr:
            print("UP")
        elif dc > posc:
            print("RIGHT")
        elif dc < posc:
            print("LEFT")
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)