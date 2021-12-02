INPUT = "input.txt"
if __name__=="__main__":
    count = 0
    with open(INPUT) as fp:
        prev_depth = int(next(fp))
        for line in fp:
            new_depth = int(line)
            if new_depth > prev_depth:
                count += 1
            prev_depth = new_depth
    print(count)
