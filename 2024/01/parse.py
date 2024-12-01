l1 = []
l2 = []
with open('input.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip()
        i1, i2 = line.split()
        i1 = int(i1)
        i2 = int(i2)
        l1.append(i1)
        l2.append(i2)
sorted_l1 = sorted(l1)
sorted_l2 = sorted(l2)
diff = 0
for i in range(len(sorted_l1)):
    diff += abs(sorted_l1[i] - sorted_l2[i])
print(diff)


sum2 = 0
for i1 in l1:
    cnt = 0
    for i2 in l2:
        if i1 == i2:
            cnt += 1
    mult = i1 * cnt
    sum2 += mult
print(sum2)

