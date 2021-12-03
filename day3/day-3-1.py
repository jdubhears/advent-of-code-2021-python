with open('input1.txt') as f:
    lines = f.readlines()

#strip newline and whitespace characters
bit_length = len(lines[0].strip())

bit_dictionary = {i: [] for i in range(bit_length)}

for line in lines:
    #strip newline and whitespace characters to line up with bit length
    line = line.strip()
    for i in range(bit_length):
        bit_dictionary[i].append(int(line[i]))

gamma_rate = ''
for list in bit_dictionary.values():
    ones_count = list.count(1)
    if ones_count > (len(lines)/2):
        gamma_rate = gamma_rate + '1'
    else:
        gamma_rate = gamma_rate + '0'

gamma_dec = int(gamma_rate, 2)

print('Gamma rate: ', gamma_dec)

epsilon_rate = ''
for char in gamma_rate:
    if char == '1':
        epsilon_rate = epsilon_rate + '0'
    elif char == '0':
        epsilon_rate = epsilon_rate + '1'

epsilon_dec = int(epsilon_rate, 2)

print('Epsilon rate: ', epsilon_dec)

power = gamma_dec * epsilon_dec

print('Power: ', power)

