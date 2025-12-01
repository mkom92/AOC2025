# AOC 2025 day 1

inp_array = [line.strip() for line in open('input.txt', 'r')]

def star_1(inp_array):    

    position, zeroes = 50, 0

    for move in inp_array:
        position += ((move[0] == 'L') * (-1) + (move[0] == 'R') * (1)) * int(move[1:])

        if position == 0 or position%100 == 0:
            zeroes += 1
            position = 0

        elif position > 100:
            position = position%100

        else:
            position = 100 - (-1 * position)%100
    
    return zeroes


def star_2(inp_array):

    position, zeroes = 50, 0

    for move in inp_array:

        position += ((move[0] == 'L') * (-1) + (move[0] == 'R') * (1)) * int(move[1:])

        if position < 0:
            zeroes += -1 * (position//100) - (1 if position == -int(move[1:]) else 0)
            position = 100 - (-1 * position)%100

        if position == 0:
            zeroes += 1

        elif position >= 100:
            zeroes += position//100
            position = position%100

    return zeroes

if __name__ == '__main__':
    print(f'Star 1: {star_1(inp_array)}')
    print(f'Star 2: {star_2(inp_array)}')