#INPUT = "test.txt"
INPUT = "input.txt"

def get_final_pos(filename):
    h, d = 0, 0
    with open(filename) as fp:
        for line in fp:
            sp = line.split(" ")
            if sp[0] == 'forward':
                h += int(sp[1])
            elif sp[0] == 'down':
                d += int(sp[1])
            elif sp[0] == 'up':
                d -= int(sp[1])
    return h, d

if __name__ == "__main__":
    h, d = get_final_pos(INPUT)
    print(h, d, h*d)
