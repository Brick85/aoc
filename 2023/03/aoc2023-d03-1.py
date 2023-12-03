def read_input(test=False):
    if test:
        filename = "test.dat"
    else:
        filename = "input.dat"
    with open(filename) as f:
        return f.read().splitlines()


def find_next_number(line, start):
    s = e = None
    for i in range(start or 0, len(line)):
        check = "0123456789"
        if s is None:
            check += "-"
        if line[i] in check:
            if s is None:
                s = i
            e = i + 1
        elif e is not None:
            break
    if e is not None:
        return s, e
    return None, None


def check_symbol(symbol):
    if symbol in "0123456789":
        return True
    if symbol != ".":
        return True
    return False


def is_part(data, line, s, e):
    if s > 0:
        if check_symbol(data[line][s - 1]):
            return True
        s -= 1
    if e < len(data[line]):
        if check_symbol(data[line][e]):
            return True
        e += 1
    cs = max(0, s - 1)
    ce = min(len(data[line]), e)
    for i in range(cs, ce):
        if line > 0:
            if check_symbol(data[line - 1][i]):
                return True
        if line < len(data) - 1:
            if check_symbol(data[line + 1][i]):
                return True
    return False


def print_part(line, s, e, data):
    if s > 0:
        s -= 1
    if e < len(data[line]):
        e += 1
    if line > 0:
        print(data[line - 1][s:e])
    print(data[line][s:e])
    if line < len(data) - 1:
        print(data[line + 1][s:e])


def main():
    data = read_input(test=False)
    w = len(data[0])
    h = len(data)
    current_line = 0
    s = e = 0
    num_locations = []
    while current_line < h:
        s, e = find_next_number(data[current_line], e)
        if s is None:
            current_line += 1
            continue
        if data[current_line][e - 1] == "-":
            continue
        num_locations.append((current_line, s, e))
    sum = 0
    for line, s, e in num_locations:
        part = False
        if is_part(data, line, s, e):
            part = True
            num = data[line][s:e]
            sum += int(num)
        print("!!!", data[line][s:e], part)
        print_part(line, s, e, data)
    print(sum)


if __name__ == "__main__":
    main()
