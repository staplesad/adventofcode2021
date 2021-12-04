#INPUT = "test.txt"
INPUT = "input.txt"

def score(mat, marked):
    score = 0
    for row in mat:
        for val in row:
            if val not in marked:
                score += val
    return score*marked[-1]


def check_bingo(board):
    dim = len(board)
    if any(sum(row)==dim for row in board):
        return True
    if any(sum(row)==dim for row in zip(*board)):
        return True
    return False

def find_winning(boards, draws):
    dim = len(boards[0])
    marked = []
    tracked = [[[0]*dim]*dim for _ in boards]
    found = []
    for n in draws:
        marked.append(n)
        for k, board in enumerate(boards):
            if k in found:
                continue
            for i, row in enumerate(board):
                tracked[k][i] = [1 if board[i][j] == n else val
                        for j, val in enumerate(tracked[k][i])]
            if check_bingo(tracked[k]):
                winning = board
                found += [k]
                if len(found) == len(boards):
                    break
        if len(found) == len(boards):
            break
    return winning, marked

def read_board(lines):
    board = []
    for line in lines:
        line = [c for c in line.split(" ") if c]
        line = list(map(int, map(lambda x: x.strip(), line)))
        board.append(line)
    return board

def solve(filename):
    boards = []
    with open(filename) as fp:
        draws = next(fp).split(',')
        _ = next(fp)
        tmp = []
        for line in fp:
            if line.strip():
                tmp.append(line)
            else:
                boards.append(read_board(tmp))
                tmp = []
        if tmp:
            boards.append(read_board(tmp))

    draws = list(map(int, draws))
    winning_board, marked = find_winning(boards, draws)
    return score(winning_board, marked)

if __name__ == "__main__":
    print(solve(INPUT))
