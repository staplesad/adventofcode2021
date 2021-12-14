from functools import reduce

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
    return [(i, j) for i, j in adj]

def clean_basins(b_list, matrix):
    basins = []
    for b in b_list:
        visited_set = b
        basins.append((len(visited_set), visited_set))
    return basins

def find_basins(low_points, matrix):
    basin_list = []
    start_points = [(i, j) for i, j in low_points]
    for s in start_points:
        frontier = [s]
        basin_points = set()
        while frontier:
            nfront = []
            for point in frontier:
                next_points = get_adj(matrix, point[0], point[1])
                if point in basin_points:
                    continue
                if matrix[point[0]][point[1]]==9:
                    continue
                basin_points.add(point)
                nfront.extend(next_points)
            if not nfront:
                basin_list.append(basin_points)
            frontier = nfront
    return clean_basins(basin_list, matrix)

def solve(input_matrix):
    low_points = []
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[0])):
            val = input_matrix[i][j]
            if all(val < input_matrix[n[0]][n[1]] for n in get_adj(input_matrix, i, j)):
                low_points.append((i,j))
    basin_list = find_basins(low_points, input_matrix)
    basin_size_sorted = sorted([b[0] for b in basin_list], reverse=True)
    return reduce(lambda x, y: x*y, basin_size_sorted[:3])

if __name__=="__main__":
    mat = read_input(INPUT)
    soln = solve(mat)
    print(soln)
