_x, _y = map(int, input().split())

# insert chess table
chess_table = []
for _ in range(_x):
    chess_table.append(input())

# calculation
workload_qty_possibilities = []
for _x_inspect in range(_x - 7):            # cut x into x_length as 8
    for _y_inspect in range(_y - 7):        # cut y into y_length as 8
        black_coloring_qty = 0              # if I start coloring with [WHITE] on the first tile
        white_coloring_qty = 0              # if I start coloring with [BLACK] on the first tile 
        
        # check one by one amid the cut pieces of the larger chess board
        for _x_turn in range(_x_inspect, _x_inspect + 8):
            for _y_turn in range(_y_inspect, _y_inspect + 8):
                if (_x_turn + _y_turn) % 2 == 0:        # should same with the first tile
                    if chess_table[_x_turn][_y_turn] != "W":
                        white_coloring_qty += 1
                    else:
                        black_coloring_qty += 1
                else:
                    if chess_table[_x_turn][_y_turn] != "W":
                        black_coloring_qty += 1
                    else:
                        white_coloring_qty += 1

        workload_qty_possibilities.append(white_coloring_qty)
        workload_qty_possibilities.append(black_coloring_qty)

print(min(workload_qty_possibilities))