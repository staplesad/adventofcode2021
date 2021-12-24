hex_map = { '0' : [0, 0, 0, 0],
            '1' : [0, 0, 0, 1],
            '2' : [0, 0, 1, 0],
            '3' : [0, 0, 1, 1],
            '4' : [0, 1, 0, 0],
            '5' : [0, 1, 0, 1],
            '6' : [0, 1, 1, 0],
            '7' : [0, 1, 1, 1],
            '8' : [1, 0, 0, 0],
            '9' : [1, 0, 0, 1],
            'A' : [1, 0, 1, 0],
            'B' : [1, 0, 1, 1],
            'C' : [1, 1, 0, 0],
            'D' : [1, 1, 0, 1],
            'E' : [1, 1, 1, 0],
            'F' : [1, 1, 1, 1]}

INPUT = "test.txt"

def read_input(filename):
    with open(filename) as fp:
        hex_lst = list(next(fp).strip())
    return hex_lst


def hex2bin(hex_lst):
    bin_lst = []
    for c in hex_lst:
        bin_lst.extend(hex_map[c])
    return bin_lst

def bin2dec(bin_lst):
    dec = 0
    for i, d in enumerate(bin_lst[::-1]):
        dec += (2**i)*d
    return dec

def get_version_num(bin_lst):
    return bin_lst[:3]

def get_t_num(bin_lst):
    return bin_lst[3:6]

def parse_operator(bin_lst):
    V = bin2dec(get_version_num(bin_lst))
    length = bin_lst[6]
    if length == 0:
        n_bits = 15
    elif length == 1:
        n_bits = 11
    L = bin2dec(bin_lst[7:7+n_bits])
    children_lst, remaining = parse_children(bin_lst[7+n_bits:], L, length)
    return V, children_lst, remaining

def parse_literal(bin_lst):
    V = bin2dec(get_version_num(bin_lst))
    child_lst = []
    i = 0
    prefix = True
    while prefix:
        n = bin_lst[6+i*5:6+i*5+5]
        child_lst.extend(n)
        if n[0] == 0:
            prefix=False
        i += 1
    return V, len(child_lst)+6, bin_lst[6+i*5:]

def parse_children(bin_lst, L, length):
    if length == 0 and L == 0:
        return [], bin_lst
    if length == 1 and L == 0:
        return [], bin_lst
    T = bin2dec(get_t_num(bin_lst))
    print('parse children', L)
    if T == 4:
        print('literal')
        V, len_lit, remaining = parse_literal(bin_lst)
        if length == 0:
            L = L - len_lit
        elif length == 1:
            L = L - 1
        print(remaining, L, length)
        children_lst, not_parsed = parse_children(remaining, L, length)
    else:
        print('operator')
        V, children_lst, not_parsed = parse_operator(bin_lst)
#        if not_parsed:
#            sibling_lst, not_parsed = parse_children(not_parsed)
#            children_lst += sibling_lst
    return [V] + children_lst, not_parsed

def solve(hex_lst):
    bin_lst = hex2bin(hex_lst)
    T = bin2dec(get_t_num(bin_lst))
    print('Solve', T)
    children_lst = []
    if T == 4:
        V, _, _ = parse_literal(bin_lst)
    else:
        V, children_lst, _ = parse_operator(bin_lst)
    Vsum = sum([V] + children_lst)
    return Vsum

if __name__=='__main__':
    hex_lst = read_input(INPUT)
    soln = solve(hex_lst)
    print(soln)
