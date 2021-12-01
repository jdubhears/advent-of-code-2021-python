previous_number = 0
counter = 0
with open('input1.txt') as f:
    for line in f:
        number = int(line)
        
        if number > previous_number:
            counter += 1

        previous_number = number

#subtract 1 since the first depth will always be higher than 0
counter = counter - 1
print('The depth increased this many times: ', counter)