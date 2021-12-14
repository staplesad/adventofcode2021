from collections import Counter

INPUT = "input.txt"
n_steps = 10

def read_input(filename):
    rules = []
    with open(filename) as fp:
        template = next(fp)
        for line in fp:
            if line.strip() !="":
                line = line.split('->')
                line = tuple(l.strip() for l in line)
                rules.append(line)
    return template, rules

def step(t, r_dict):
    indices = []
    new_string = ""
    for i in range(len(t)):
        if t[i:i+2] in r_dict:
            new_string += r_dict[t[i:i+2]]
        else:
            new_string += t[i]
    return new_string

def solve(t, r):
    ns = t
    rules_dict = {k: k[0] + v for k,v in rules}
    for _ in range(n_steps):
        ns = step(ns, rules_dict)
    counts = Counter(ns.strip()).most_common()
    print(counts[0], counts[-1])
    return counts[0][1] - counts[-1][1]

if __name__=='__main__':
    template, rules = read_input(INPUT)
    print(template, rules)
    soln = solve(template, rules)
    print(soln)

