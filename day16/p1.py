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
    while prefix:
        idx = 6+i*5
        chunk = bin_lst[idx:idx+5]
        if chunk[0] == 0:
            prefix = False
        i += 1
    return [V], bin_lst[6+i*5:]

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
    while L > 0:
        if len(new_bin_lst) < 7:
            print(new_bin_lst, L)
            break
        T = bin2dec(get_t_num(new_bin_lst))
        if T == 4:
            childVs, remaining = parse_literal(new_bin_lst)
        else:
            childVs, remaining = parse_operator(new_bin_lst)
        Vs.extend(childVs)
        if I == 0:
            L -= (len(new_bin_lst) - len(remaining))
        elif I == 1:
            L -= 1
        new_bin_lst = remaining
    return Vs, remaining

def parse_packet(bin_lst):
    T = bin2dec(get_t_num(bin_lst))
    if T == 4:
        Vs, remaining = parse_literal(bin_lst)
    else:
        Vs, remaining = parse_operator(bin_lst)
    if len(remaining)>11:
        nextV = parse_packet(remaining)
    else:
        nextV = []
    return Vs + nextV

def solve(bin_lst):
    Vs = parse_packet(bin_lst)
    return sum(Vs)

if __name__=='__main__':
    hex_lst = read_input(INPUT)
    bin_lst = hex2bin(hex_lst)
    soln = solve(bin_lst)
    print(soln)
