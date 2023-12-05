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
            if seed >= line[1] and seed < line[2]:
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
    # smallest = None
    # a = 0
    # # seeds = seeds[:4]
    # total = 0
    # min = float("inf")
    # max = 0
    # while a <= len(seeds) - 1:
    #     if seeds[a] < min:
    #         min = seeds[a]
    #     if seeds[a] + seeds[a + 1] > max:
    #         max = seeds[a] + seeds[a + 1]
    #     a += 2
    # a = 0
    # print(min, max)
    # print(max - min)
    # while a <= len(seeds) - 1:
    #     print(seeds[a], seeds[a] + seeds[a + 1])
    #     for seed in range(seeds[a], seeds[a] + seeds[a + 1]):
    #         seed = get_seed_location(seed, ranges)
    #         total += 1
    #         if total % 1000000 == 0:
    #             print("total", total)
    #         if smallest is None or seed < smallest:
    #             print("found seed", seed)
    #             smallest = seed
    #     a += 2
    # print(smallest)

    seed_ranges = []
    i = 0
    while i <= len(seeds) - 1:
        seed_ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))
        i += 2

    # print(seed_ranges)
    from_nul = False

    rangeinfos = list(reversed(sorted(ranges[-1], key=lambda x: x[1])))
    rangeinfo = rangeinfos[0]

    # again super unefficent, but it makes work done in few minutes.
    # maybe I'll do more optimal solution with ranges later...

    for i in range(0, rangeinfo[1] + rangeinfo[2]):
        # for i in range(45, 48):
        # print("\n\nloc", i)
        if i % 1000000 == 0:
            print("i", i)
        value = loc_to_seed(i, ranges)
        for seed_range in seed_ranges:
            if value in seed_range:
                print(i, value, seed_range)
                return


def loc_to_seed(item, ranges):
    for rangeinfo in reversed(ranges):
        init = item
        for line in rangeinfo:
            if item >= line[0] and item < line[0] + line[2]:
                item = line[1] + (item - line[0])
                break
        # print(init, "->", item)
    return item


if __name__ == "__main__":
    main()
