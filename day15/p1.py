INPUT = "input.txt"

def read_input(filename):
    mat = []
    with open(filename) as fp:
        for line in fp:
            mat.append(list(map(int, line.strip())))
    return mat


def solve(mat):
    frontier = [((0, 1), 0), ((1, 0), 0)]
    visited = {}
    path_risk = None
    while frontier:
        (y, x), risk  = frontier.pop()
        if y >= len(mat) or y < 0:
            continue
        if x >= len(mat[0]) or x < 0:
            continue
        nrisk = mat[y][x] + risk
        if path_risk and nrisk > path_risk:
            continue
        if (y, x) in visited:
            if visited[(y, x)] <= nrisk:
                continue
        visited[(y, x)] = nrisk
        if y==(len(mat)-1) and x==(len(mat[0])-1):
            if not path_risk or nrisk < path_risk:
                path_risk = nrisk
        else:
            new_points = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
            frontier.extend([(point, nrisk) for point in new_points])
    return path_risk

if __name__ == '__main__':
    mat = read_input(INPUT)
    soln = solve(mat)
    print(soln)
