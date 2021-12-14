from operator import itemgetter
from collections import defaultdict

INPUT = "input.txt"
n_steps = 40

def read_input(filename):
    rules = []
    with open(filename) as fp:
        template = next(fp).strip()
        for line in fp:
            if line.strip() !="":
                line = line.split('->')
                line = tuple(l.strip() for l in line)
                rules.append(line)
    return template, rules

def step(t_dict, r_dict, char_dict):
    dict_update = defaultdict(int)
    for pair in t_dict:
        dict_update[pair] += t_dict[pair]
        if pair in r_dict:
            np_1 = r_dict[pair][0]
            np_2 = r_dict[pair][1]
            char_dict[np_1[1]] += t_dict[pair]

            dict_update[np_1] += t_dict[pair]
            dict_update[np_2] += t_dict[pair]
            dict_update[pair] -= t_dict[pair]
    t_dict.update(dict_update)
    return t_dict

def get_ttuples(t):
    for i in range(len(t)-1):
        yield t[i:i+2]

def count_chars(char_dict):
    sorted_t = sorted(char_dict.items(), key=itemgetter(1))
    return sorted_t[-1][1], sorted_t[0][1]

def solve(t, r):
    t_dict = defaultdict(int)
    for pair in get_ttuples(t):
        t_dict[pair] += 1

    char_dict = defaultdict(int)
    for c in t:
        char_dict[c] += 1

    ndict = t_dict
    rules_dict = {k: (k[0] + v, v + k[1]) for k,v in rules}
    for _ in range(n_steps):
        ndict = step(ndict, rules_dict, char_dict)
        for k in [k for k in ndict if ndict[k]==0]:
            if ndict[k] == 0:
                ndict.pop(k)
    counts = count_chars(char_dict)
    return counts[0] - counts[1]

if __name__=='__main__':
    template, rules = read_input(INPUT)
    print(template, rules)
    soln = solve(template, rules)
    print(soln)

