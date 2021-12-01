previous_sum = 0
counter = 0
with open('input1.txt') as f:
    lines = f.readlines()

    #subtract 2 from length of file since we need to grab groupings of 3
    for i in range(len(lines) - 2):
        int1 = int(lines[i])
        int2 = int(lines[i + 1])
        int3 = int(lines[i + 2])

        total = int1 + int2 + int3

        if total > previous_sum:
            counter += 1

        previous_sum = total

#subtract 1 since the first total will always be higher than 0
counter = counter - 1
print('The triple sum increased this many times: ', counter)