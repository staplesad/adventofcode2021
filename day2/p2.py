#INPUT = "test.txt"
INPUT = "input.txt"

def get_final_pos(filename):
    h, d, aim = 0, 0, 0
    with open(filename) as fp:
        for line in fp:
            sp = line.split(" ")
            if sp[0] == 'forward':
                h += int(sp[1])
                d += int(sp[1])*aim
            elif sp[0] == 'down':
                aim += int(sp[1])
            elif sp[0] == 'up':
                aim -= int(sp[1])
    return h, d

if __name__ == "__main__":
    h, d = get_final_pos(INPUT)
    print(h, d, h*d)
