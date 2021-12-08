from collections import defaultdict
INPUT = "input.txt"

def get_easy_digits(output_vals):
    lens = {2: 1, 3:7, 4:4, 7:8}
    digits = {}
    for val in output_vals:
        if len(val) in lens:
            digits[lens[len(val)]] = val
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

def get_other_digits(output_vals):
    lens = [5, 6]
    digits = defaultdict(list)
    for val in output_vals:
        if len(val) in lens:
            digits[len(val)].append(val)
    return digits

def get_segments(seq, digits):
    a = list(set(digits[7]) - set(digits[1]))[-1]
    bd = list(set(digits[4]) - set(digits[1]))
    eg = list((set(digits[8]) - set(digits[4])) - set([a]))
    len_digs = get_other_digits(seq[0])
    digits[5] = [val for val in len_digs[5] if all(l in val for l in bd)][-1]
    c = list(set(digits[8]) - set(digits[5]) - set(eg))[-1]
    f = list(set(digits[1]) - set([c]))[-1]
    digits[2] = [val for val in len_digs[5] if f not in val][-1]
    digits[3] = [val for val in len_digs[5]
                 if val not in digits[2] and val not in digits[5]][-1]
    digits[0] = [val for val in len_digs[6] if not all(l in val for l in bd)][-1]
    digits[6] = [val for val in len_digs[6]
                 if val not in digits[0] and c not in val][-1]
    digits[9] = [val for val in len_digs[6]
                 if val not in digits[0] and val not in digits[6]][-1]
    return digits

def translate(seq, digits):
    numbers = []
    for s in seq:
        d = digits["".join(sorted(s))]
        numbers.append(d)
    numbers = map(str, numbers)
    nstr = "".join(numbers)
    return int(nstr)

def solve(inputs):
    count = 0
    for lst in inputs:
        digits = get_easy_digits(lst[0])
        digits = get_segments(lst, digits)
        rev_digits = {"".join(sorted(val)):k for k, val in digits.items()}
        new_digits = translate(lst[1], rev_digits)
        count += new_digits
    return count

if __name__ == "__main__":
    input_val = read_input(INPUT)
    soln = solve(input_val)
    print(soln)
