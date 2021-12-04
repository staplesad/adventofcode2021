from collections import Counter

#INPUT = "test.txt"
INPUT = "input.txt"

def bin_to_dec(n_list):
    n = 0
    for i, dig in enumerate(n_list[::-1]):
        n += pow(2, i)*dig
    return n

def solve(filename):
    with open(filename) as fp:
        numbers = []
        for line in fp:
            n = list(line)[:-1]
            n = list(map(int, n))
            numbers.append(n)
        transpose_n = list(zip(*numbers))
        g = list(map(lambda x: x.most_common()[0][0], map(Counter, transpose_n)))
        e = list(map(lambda x: x.most_common()[1][0], map(Counter, transpose_n)))
        return g, e

if __name__=="__main__":
    g, e = solve(INPUT)
    print(g, e)
    print(bin_to_dec(g), bin_to_dec(e), bin_to_dec(g)*bin_to_dec(e))
