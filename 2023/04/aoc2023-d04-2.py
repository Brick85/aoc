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
    dataout = []
    for line in data:
        id, nums_w, nums = get_data(line)
        score = 0
        for num in nums:
            if num in nums_w:
                score += 1
        dataout.append(score)
    sum = 0
    # very unoptimized, but works for single use
    for i in range(len(dataout)):
        sum += count_sum(dataout[i:])
    print(sum)

def count_sum(data):
    if len(data) == 0:
        return 0
    sum = 1
    # print(data[0])
    for i in range(data[0]):
        sum += count_sum(data[i+1:])
    return sum

if __name__ == "__main__":
    main()

