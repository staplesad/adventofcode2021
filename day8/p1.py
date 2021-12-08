from collections import defaultdict
from itertools import chain

INPUT = "input.txt"

def get_easy_digits(output_vals):
    lens = {2: 1, 3:7, 4:4, 7:8}
    digits = defaultdict(list)
    for val in output_vals:
        if len(val) in lens:
            digits[lens[len(val)]].append(val)
    return digits

def read_input(filename):
    inputs = []
    with open(filename) as fp:
        for line in fp:
            halves = line.split('|')
            halves = [l.split(" ") for l in halves]
            halves = [[w.strip() for w in l if w.strip()] for l in halves]
            inputs.append((halves[0], halves[1]))
    return inputs

def solve(inputs):
    digits = []
    for lst in inputs:
        digits.extend(chain(*get_easy_digits(lst[1]).values()))
    return len(digits)

if __name__ == "__main__":
    input_val = read_input(INPUT)
    soln = solve(input_val)
    print(soln)
