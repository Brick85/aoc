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
    a = 0
    seeds_sets = []
    while a < len(seeds):
        seeds_sets.append((seeds[a], seeds[a+1]))
        a += 2

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

    outs = []
    for start, size in seeds_sets:
        # print("### start ###")
        outs += get_ranges(start, size, ranges)
    outs.sort()
    print(outs[0][0])

def get_ranges(start, size, ranges):
    msg = "get_ranges", start, size, len(ranges)
    if len(ranges) == 0:
        return [(start, size)]
    out = []
    current_range = ranges[0]
    for line in current_range:
        r_size = line[2]
        r_in_from = line[1]
        r_in_to = line[1] + line[2]
        r_out_from = line[0]
        r_out_to = line[0] + line[2]

        if start >= r_in_from and start < r_in_to:
            nstart = start - r_in_from + r_out_from
            if start+size <= r_in_to:
                # print(msg, "fr - fits all range", line, start, size)
                out += get_ranges(nstart, size, ranges[1:])
            else:
                nsize = r_out_to - nstart
                # print(msg, "fr - fits part of range", line, start, nsize) 
                out += get_ranges(nstart, nsize, ranges[1:])
                # print(msg, "fr - part2", r_in_to, size - nsize) 
                out += get_ranges(r_in_to, size - nsize, ranges)
            return out
    # print(msg, "no fit found")
    out += get_ranges(start, size, ranges[1:])
    return out
    
if __name__ == "__main__":
    main()
