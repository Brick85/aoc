import sys


def read_input(test=False):
    if test:
        filename = "test.dat"
    else:
        filename = "input.dat"
    with open(filename) as f:
        return f.read().splitlines()


def main():
    test = False
    if len(sys.argv) == 2 and sys.argv[1] == "test":
        test = True
    data = read_input(test=test)
    process(data)


def get_seed_location(seed, ranges):
    for rangeinfo in ranges:
        for line in rangeinfo:
            if seed >= line[1] and seed < line[1] + line[2]:
                seed = line[0] + (seed - line[1])
                break
    return seed


def process(data):
    seeds = data[0].split(":")[1]
    seeds = [int(x.strip()) for x in seeds.split()]

    ranges = []
    for line in data[1:]:
        if line.endswith("map:"):
            rangeinfo = []
            ranges.append(rangeinfo)
        elif line.strip():
            a, b, c = line.split()
            a = int(a)
            b = int(b)
            c = int(c)
            rangeinfo.append((a, b, c))
    smallest = float("inf")
    for seed in seeds:
        loc = get_seed_location(seed, ranges)
        if loc < smallest:
            smallest = loc
    print(smallest)


if __name__ == "__main__":
    main()
