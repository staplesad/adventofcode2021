from functools import reduce

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

INPUT = "input.txt"

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

def parse_literal(bin_lst):
    V = bin2dec(get_version_num(bin_lst))
    prefix = True
    i = 0
    current = []
    while prefix:
        idx = 6+i*5
        chunk = bin_lst[idx:idx+5]
        current.extend(chunk[1:])
        if chunk[0] == 0:
            prefix = False
        i += 1
    current = [bin2dec(current)]
    return current, [V], bin_lst[6+i*5:]

def parse_operator(bin_lst):
    V = bin2dec(get_version_num(bin_lst))
    I = bin_lst[6]
    if I == 0:
        final_bit = 7+15
    elif I == 1:
        final_bit = 7+11
    L = bin2dec(bin_lst[7:final_bit])
    new_bin_lst = bin_lst[final_bit:]
    remaining = new_bin_lst
    Vs = [V]
    values = []
    while L > 0:
        if len(new_bin_lst) < 7:
            print(new_bin_lst, L)
            break
        T = bin2dec(get_t_num(new_bin_lst))
        if T == 4:
            current, childVs, remaining = parse_literal(new_bin_lst)
        else:
            current, childVs, remaining = parse_operator(new_bin_lst)
        Vs.extend(childVs)
        values.extend(current)
        if I == 0:
            L -= (len(new_bin_lst) - len(remaining))
        elif I == 1:
            L -= 1
        new_bin_lst = remaining
    print(values)
    T = bin2dec(get_t_num(bin_lst))
    if T == 0:
        current = [sum(values)]
    elif T == 1:
        current = [reduce(lambda x, y: x*y, values)]
    elif T == 2:
        current = [min(values)]
    elif T == 3:
        current = [max(values)]
    elif T == 5:
        current = [1 if values[0] > values[1] else 0]
    elif T == 6:
        current = [1 if values[0] < values[1] else 0]
    elif T == 7:
        current = [1 if values[0] == values[1] else 0]

    return current, Vs, remaining

def parse_packet(bin_lst):
    T = bin2dec(get_t_num(bin_lst))
    if T == 4:
        c, Vs, remaining = parse_literal(bin_lst)
    else:
        c, Vs, remaining = parse_operator(bin_lst)
    if len(remaining)>11:
        nextC = parse_packet(remaining)
    else:
        nextC = []
    return c + nextC

def solve(bin_lst):
    Vs = parse_packet(bin_lst)
    print(Vs)
    return sum(Vs)

if __name__=='__main__':
    hex_lst = read_input(INPUT)
    bin_lst = hex2bin(hex_lst)
    soln = solve(bin_lst)
    print(soln)
