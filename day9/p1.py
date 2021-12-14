INPUT = "input.txt"

def risk(h):
    return h+1

def read_input(filename):
    mat = []
    with open(filename) as fp:
        for line in fp:
            line = list(map(int, list(line.strip())))
            mat.append(line)
    return mat

def get_adj(mat, i, j):
    adj = [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]
    pop = []
    if i == 0:
        pop.append(2)
    elif i == len(mat)-1:
        pop.append(3)
    if j == 0:
        pop.append(0)
    elif j == len(mat[0])-1:
        pop.append(1)
    pop = sorted(pop, reverse=True)
    for p in pop:
        _ = adj.pop(p)
    return [mat[i][j] for i, j in adj]

def solve(input_matrix):
    low_points = []
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[0])):
            val = input_matrix[i][j]
            adj = get_adj(input_matrix, i, j)
            if all(val < n for n in get_adj(input_matrix, i, j)):
                low_points.append(val)
    return sum(map(risk, low_points))

if __name__=="__main__":
    mat = read_input(INPUT)
    soln = solve(mat)
    print(soln)
