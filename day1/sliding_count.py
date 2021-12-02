# INPUT = "test.txt"
INPUT = "input.txt"

def ovrlap_windows(flat, n):
    for i in range(len(flat) - n + 1):
        yield flat[i:i+n]

def sliding_windows(filename):
    depths = []
    with open(filename) as fp:
        for line in fp:
            depths.append(int(line))
    windows = ovrlap_windows(depths, 3)
    summed = list(map(sum, windows))
    count = 0
    prev_depth = summed[0]
    for x in summed[1:]:
        if x > prev_depth:
            count += 1
        prev_depth = x
    return count

if __name__=="__main__":
    print(sliding_windows(INPUT))
