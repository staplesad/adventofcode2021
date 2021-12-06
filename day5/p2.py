INPUT = "input.txt"

def expand(start, end):
    if start[0] == end[0]:
        max_y = max(start[1], end[1])
        min_y = min(start[1], end[1])
        return [(start[0], i) for i in range(min_y, max_y+1, 1)]
    if start[1] == end[1]:
        max_x = max(start[0], end[0])
        min_x = min(start[0], end[0])
        return [(i, start[1]) for i in range(min_x, max_x+1, 1)]
    dx = -1 if start[0] >= end[0] else 1
    dy = -1 if start[1] >= end[1] else 1
    points = list(zip(list(range(start[0], end[0]+dx, dx)),
                      list(range(start[1], end[1]+dy, dy))))
    return points

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
