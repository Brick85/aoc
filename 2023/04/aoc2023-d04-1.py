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
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test = True
    data = read_input(test=test)
    process(data)

def get_data(line):
    id, data = line.split(':')
    id = int(id.split()[1].strip())
    nums_w, nums = data.split('|')
    nums_w = [int(x.strip()) for x in nums_w.split()]
    nums = [int(x.strip()) for x in nums.split()]
    return id, nums_w, nums

def process(data):
    sum = 0
    for line in data:
        id, nums_w, nums = get_data(line)
        score = 0
        for num in nums:
            if num in nums_w:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        sum += score
    print(sum)

if __name__ == "__main__":
    main()

