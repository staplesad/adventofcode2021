from collections import Counter

INPUT = "input.txt"

def step(counter):
    new_fish = counter.get(0, 0)
    new_counter = {k-1: n for k,n in counter.items() if k!=0}
    new_counter[8] = new_fish
    new_counter[6] = new_counter.get(6, 0) + new_fish
    return new_counter

def multi_step(counter, n_days):
    for i in range(n_days):
        counter = step(counter)
    return counter

def solve(filename):
    with open(filename) as fp:
        line = next(fp)
        init = list(map(int, line.split(',')))
    fish_counter = dict(Counter(init))
    final_counter = multi_step(fish_counter, n_days=80)
    return sum(final_counter.values())

if __name__ == '__main__':
    print(solve(INPUT))

