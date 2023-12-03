import sys

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
        # if s is None:
        #     check += "-"
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
        return False
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
    cs = max(0, s)
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

def is_str_num(ch):
    return ch in '0123456789'


def get_num(line, x):
    s = e = x
    while s > 0 and is_str_num(line[s-1]):
        s -= 1
    while e < len(line) and is_str_num(line[e]):
        e += 1
    return int(line[s:e])

def get_gear(data, x, y):
    nums = []
    tl = data[y-1]
    ll = data[y]
    bl = data[y+1]
    for line in [tl, ll, bl]:
        if is_str_num(line[x-1]) and not is_str_num(line[x]) and is_str_num(line[x+1]):
            nums.append(get_num(line, x-1))
            nums.append(get_num(line, x+1))
        elif is_str_num(line[x-1]):
            nums.append(get_num(line, x-1))
        elif is_str_num(line[x]):
            nums.append(get_num(line, x))
        elif is_str_num(line[x+1]):
            nums.append(get_num(line, x+1))
    if len(nums) == 2:
        return nums[0] * nums[1]
    return 0

def main():
    test = False
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test = True
    data = read_input(test=test)
    w = len(data[0])
    h = len(data)
    sum = 0
    for y in range(h):
        for x in range(w):
            if data[y][x] == "*":
                sum += get_gear(data, x, y)
    print(sum)


if __name__ == "__main__":
    main()
