import re

letter_nums = {
    # "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
letter_nums_teen = {
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eightteen": 18,
    "nineteen": 19,
}
letter_nums_tens = {
    "twenty": 20,
    "thirty": 30,
    "fourty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
}
letter_nums2 = {
    # "zero": 0,
    "one": "on1e",
    "two": "tw2o",
    "three": "th3ree",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "se7ven",
    "eight": "ei8ght",
    "nine": "ni9ne",
}
r_letter_nums = "|".join(letter_nums)


def replace_let(line):
    # line = replace_let_set(line, letter_nums_teen)
    # line = replace_let_set(line, letter_nums_tens)
    line = replace_let_set(line, letter_nums)
    return line


def replace_let_set(line, numset):
    for i in range(len(line)):
        for key in numset:
            if key in line[:i]:
                s1 = line[:i]
                s2 = line[i:]
                s1 = s1.replace(key, str(numset[key]))
                newline = s1 + s2
                return replace_let(newline)
    return line


def replace_let2(line):
    for key, value in letter_nums2.items():
        line = line.replace(key, str(value))
    return line


with open("input.txt") as f:
    sum = 0
    for line in f:
        print(line.strip())
        # line = replace_let(line)
        line = replace_let2(line)
        print(line.strip())
        nums = re.findall(r"[\d]", line)
        print(nums)
        first_num = None
        last_num = None
        for num in nums:
            if first_num is None:
                first_num = num
            last_num = num
        fnum = int("%s%s" % (first_num, last_num))
        sum += fnum
        print(fnum)
    print(sum)
