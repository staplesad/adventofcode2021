INPUT = "input.txt"

def expand(start, end):
    if start[0] == end[0]:
        max_p = max(start[1], end[1])
        min_p = min(start[1], end[1])
        return [(start[0], i) for i in range(min_p, max_p+1, 1)]
    if start[1] == end[1]:
        max_p = max(start[0], end[0])
        min_p = min(start[0], end[0])
        return [(i, start[1]) for i in range(min_p, max_p+1, 1)]
    return []

def str2tup(string):
    s, e = string.strip().split(',')
    return (int(s), int(e))

def solve(filename):
    count = 0
    marked = set()
    overlap = set()
    with open(filename) as fp:
        for line in fp:
            start, end = map(str2tup, line.split('->'))
            new_points = expand(start, end)
            for point in expand(start, end):
                if point in marked:
                    if not point in overlap:
                        count += 1
                        overlap.add(point)
                marked.add(point)
    return count

if __name__ == "__main__":
    print(solve(INPUT))
