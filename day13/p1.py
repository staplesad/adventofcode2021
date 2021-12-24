def read_input(filename):
    coords = []
    folds = []
    with open(filename) as fp:
        for line in fp:
            if not line.strip():
                break
            coords.append(tuple(map(int, line.strip().split(','))))
        for line in fp:
            line_fold = line.strip().split('=')
            direction = line_fold[0][-1:]
            n = int(line_fold[1])
            folds.append((direction, n))
    return coords, folds


INPUT = "input.txt"

def fold(cs, af):
    if af[0] == 'x':
        idx = 0
    else:
        idx = 1
    new_cs = []
    for c in cs:
        if c[idx] < af[1]:
            new_cs.append(c)
        else:
            new_c = list(c)
            new_c[idx] = 2*af[1] - c[idx]
            new_c = tuple(new_c)
            new_cs.append(new_c)
    return new_cs

def solve(c, f):
    new_c = fold(c, f[0])
    new_c = set(new_c)
    return len(new_c)

if __name__=='__main__':
    c, f = read_input(INPUT)
    print(c, f)
    soln = solve(c, f)

    print(soln)
