INPUT = "test.txt"
n_steps = 10

def read_input(filename):
    mat = []
    with open(filename) as fp:
        for line in fp:
            mat.append(list(map(int, line.strip())))
    return mat

def flash_impact(y, x, flash):
    for new_y, new_x in product(range(y-1, y+2), range(x-1, x+2)):
        if new_y<0 or new_y>=10:
            continue
        if new_x<0 or new_x>=10:
            continue
        if new_x==x and new_y==y:
            continue
        flash[(new_y, new_x)] += 1
    return flash

def apply_flash(new_mat, flash):
    for y in range(10):
        for x in range(10):
            if (y, x) in flash:
                new_mat[y][x] += flash[(y, x)]
                flash.pop((y, x))
                if new_mat[y][x] > 9:
                    flash = flash_impact(y, x, flash)
    return new_mat, flash

def step(mat):
    new_mat = []
    flash = defaultdict(int)
    for y in range(10):
        new_mat.append([])
        for x in range(10):
            new_mat[-1].append((mat[y][x]+1))
            if new_mat[-1][-1] > 9:
                flash = flash_impact(y, x, flash)
    while flash:
        new_mat, flash = apply_flash(new_mat, flash)
    return new_mat

def solve(matrix):
    for _ in range(n_steps):
        matrix = step(matrix)
    return matrix


if __name__=='__main__':
    mat = read_input(INPUT)
    print(len(mat), len(mat[0]))
    soln = solve(mat)
    print(soln)
