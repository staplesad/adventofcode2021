from collections import Counter

#INPUT = "test.txt"
INPUT = "input.txt"


def bin_to_dec(n_list):
    n = 0
    for i, dig in enumerate(n_list[::-1]):
        n += pow(2, i)*dig
    return n


def solve(filename):
    with open(filename) as fp:
        numbers = []
        for line in fp:
            n = list(line)[:-1]
            n = list(map(int, n))
            numbers.append(n)
        transpose_n = list(zip(*numbers))
        g = list(map(lambda x: x.most_common(), map(Counter, transpose_n)))
        co2_set = numbers
        oxygen_set = numbers
        for i in range(len(numbers[0])):
            if len(co2_set) > 1:
                digit_count_c = Counter(list(zip(*co2_set))[i]).most_common()
                if len(digit_count_c) == 1:
                    digit_c = digit_count_c[0][0]
                else:
                    digit_c = digit_count_c[-1][0] if digit_count_c[0][1] > digit_count_c[-1][1] else 0
                co2_set = [s for s in co2_set if s[i]==digit_c]
            if len(oxygen_set) > 1:
                digit_count_o = Counter(list(zip(*oxygen_set))[i]).most_common()
                if len(digit_count_o) == 1:
                    digit_o = digit_count_o[0][0]
                else:
                    digit_o = digit_count_o[0][0] if digit_count_o[0][1] > digit_count_o[1][1] else 1
                oxygen_set = [s for s in oxygen_set if s[i]==digit_o]
            if len(co2_set) == 1 and len(oxygen_set) ==1:
                break
        return co2_set[0], oxygen_set[0]


if __name__=="__main__":
    g, e = solve(INPUT)
    print(bin_to_dec(g), bin_to_dec(e), bin_to_dec(g)*bin_to_dec(e))
