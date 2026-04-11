import numpy as np 

board = np.zeros((3,3),dtype=int)

print(board)

def print_board(b):
    symbols = {0: " ", 1: "x", -1: "0"}
    for r in range(3):
        row = "  | ".join(symbols[val] for val in b[r])
        print(" "+ row)
        if r < 2:
            print("---+---+---")
            print()
print_board(board)            