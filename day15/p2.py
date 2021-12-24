INPUT = "input.txt"

def read_input(filename):
    mat = []
    with open(filename) as fp:
        for line in fp:
            mat.append(list(map(int, line.strip())))
    return mat

def make_full_matrix(mat):
    width = len(mat[0])*5
    height = len(mat)*5
    tile_w = len(mat[0])
    tile_h = len(mat)
    new_mat = []
    for j in range(5):
        for row in mat:
            new_mat.append(row*5)
    for i in range(width):
        for j in range(height):
            y_tile, x_tile = tile_dist(j, i, tile_h, tile_w)
            new_mat[j][i] = tile_risk(new_mat[j][i], y_tile, x_tile)
    return new_mat

def tile_dist(y, x, tile_h, tile_w):
    y_count = 0
    while y >= tile_h:
        y_count += 1
        y -= tile_h
    x_count = 0
    while x >= tile_w:
        x_count += 1
        x -= tile_w
    return y_count, x_count

def tile_risk(val, y_tile, x_tile):
    nval = (val + y_tile + x_tile)
    if nval > 9:
        nval = nval % 10 + 1
    return nval

def solve(mat):
    width = len(mat[0])
    height = len(mat)

    frontier = [((0, 1), 0), ((1, 0), 0)]
    visited = [[2**23 for _ in range(width)] for _ in range(height)]
    path_risk = None
    count = 0
    while frontier:
        (y, x), risk  = frontier.pop()
        if y >= height or y < 0:
            continue
        if x >= width or x < 0:
            continue
        nrisk = risk + mat[y][x]
        if path_risk and nrisk >= path_risk:
            continue
        if visited[y][x] <= nrisk:
            continue
        visited[y][x] = nrisk
        if y==(height-1) and x==(width-1):
            if not path_risk or nrisk < path_risk:
                count += 1
                print('found good end node', count, nrisk)
                path_risk = nrisk
        else:
            new_points = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
            frontier.extend([(point, nrisk) for point in new_points])
    return path_risk

if __name__ == '__main__':
    mat = read_input(INPUT)
    mat = make_full_matrix(mat)
    print(len(mat))
    print(len(mat[0]))
    soln = solve(mat)
    print(soln)
