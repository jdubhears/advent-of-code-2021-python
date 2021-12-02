#parse a line of the input and return the keyword and number
def parse_line(textline:str ):
    (keyword, number) = textline.split()
    number = int(number)
    return (keyword, number)

position = 0
depth = 0
aim = 0

with open('input1.txt') as f:
    for line in f:
        (keyword, number) = parse_line(line)
        if keyword == 'forward':
            position = position + number
            depth = depth + aim * number
        elif keyword == 'down':
            aim = aim + number
        elif keyword == 'up':
            aim = aim - number

print('Position: ', position, " Depth: ", depth)

multiply = depth * position

print('Product is: ', multiply)