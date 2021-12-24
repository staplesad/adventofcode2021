INPUT = "test.txt"

def read_input(filename):
    with open(filename) as fp:
        paths = []
        for line in fp:
            (b, e) = line.strip().split('-')
            paths.append((b, e))
            paths.append((e, b))
    return paths


def solve(paths):
    actual_paths = []
    frontier = [['start']]
    while frontier:
        nf = []
        for p in frontier:
            current_pos = p[-1]
            if current_pos == 'end':
                actual_paths.append(p)
            else:
                next_caves = [c[1] for c in paths if c[0] == current_pos]
                for c in next_caves:
                    if c.islower() and not c in p:
                        nf.append(p+[c])
                    elif not c.islower():
                        nf.append(p+[c])
        frontier = nf
    return len(actual_paths)

if __name__=='__main__':
    paths = read_input(INPUT)
    soln = solve(paths)
    print(soln)
