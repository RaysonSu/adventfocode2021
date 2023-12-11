F = open("Day 4/input.txt", "r")
F = F.readlines()

def check_bingo(board: list[list[int | str]]) -> bool:
    for i in range(len(board)):
        ret = True
        for j in range(len(board[0])):
            ret = ret and board[i][j] == "X"
        if ret:
            return ret
    
    for i in range(len(board[0])):
        ret = True
        for j in range(len(board)):
            ret = ret and board[j][i] == "X"
        if ret:
            return ret
    
    return False

def parse_input(inp: list[str]) -> tuple[list[int], list[list[list[int]]]]:
    values = []
    boards = []

    values = inp[0].split(",")
    for i in range(len(values)):
        values[i] = int(values[i])
    
    for i in range((len(inp) - 1) // 6):
        board = []
        for j in range(len(inp[2].split())):
            row = inp[6 * i + j + 2].split()
            for index in range(len(row)):
                row[index] = int(row[index])
            board.append(row)
        boards.append(board)
    
    return (values, boards)

def apply_value(board: list[list[int | str]], value: int) -> list[list[int | str]]:
    ret = []
    for row in board:
        nrow = []
        for num in row:
            if num == value:
                nrow.append("X")
            else:
                nrow.append(num)
        ret.append(nrow)
    return ret

def board_winner(boards: list[list[list[int | str]]]) -> int:
    for index in range(len(boards)):
        if check_bingo(boards[index]):
            return index
    return -1

def get_value(board: list[list[int | str]], last_value: int) -> int:
    ret = 0
    for row in board:
        for value in row:
            if value != "X":
                ret += value
    
    return ret * last_value

def remove_winners(boards):
    while board_winner(boards) != -1:
        del boards[board_winner(boards)]
    
    return boards

F = parse_input(F)

values = F[0]
boards = F[1]
last_board = []
first_board = ([], 0)

value = 0
while len(boards) > 0:
    for i in range(len(boards)):
        boards[i] = apply_value(boards[i], values[value])
        if not first_board[0] and check_bingo(boards[i]):
            first_board = (boards[i], value)
    value += 1
    last_board = boards.copy()
    boards = remove_winners(boards)

print(f"Part 1: {get_value(first_board[0], values[first_board[1]])}")
print(f"Part 2: {get_value(last_board[0], values[value - 1])}") 




