# AOC 2025 day 4

import time

def clean_area(warehouse):

    y,x = len(warehouse), len(warehouse[0])

    rolls_of_paper = []
    accessible_rolls = []

    for n, row in enumerate(warehouse):
        for m, cell in enumerate(row):
            if cell == '@':
                rolls_of_paper.append((n, m))

    for roll in rolls_of_paper:
        n, m = roll

        if roll in ((0,0), (0,x-1), (y-1,0), (y-1,x-1)):
            accessible_rolls.append(roll)
        
        elif n == 0 or n == y-1:
            area_to_check = warehouse[n][m-1] + warehouse[n][m+1] + ''.join(warehouse[n+1][m-1:m+2]) if n == 0 else ''.join(warehouse[n-1][m-1:m+2]) + warehouse[n][m-1] + warehouse[n][m+1]
            if area_to_check.count('@') < 4:
                accessible_rolls.append(roll)

        elif m == 0 or m == x-1:
            area_to_check = ''.join([warehouse[n-1][m], warehouse[n+1][m], warehouse[n-1][m+1], warehouse[n][m+1], warehouse[n+1][m+1]]) if m == 0 else ''.join([warehouse[n-1][m], warehouse[n+1][m], warehouse[n-1][m-1], warehouse[n][m-1], warehouse[n+1][m-1]])
            if area_to_check.count('@') < 4:
                accessible_rolls.append(roll)

        else:
            area_to_check = ''.join([warehouse[n-1][m-1], warehouse[n-1][m], warehouse[n-1][m+1],
                                    warehouse[n][m-1],                     warehouse[n][m+1],
                                    warehouse[n+1][m-1], warehouse[n+1][m], warehouse[n+1][m+1]])
            if area_to_check.count('@') < 4:
                accessible_rolls.append(roll)

    return len(accessible_rolls), accessible_rolls

def star_1(inp_file: str, timeit = False) -> int:

    start = time.perf_counter()

    warehouse = [[x for x in line.strip()] for line in open(inp_file, 'r')]

    accessible_count, accessible_rolls = clean_area(warehouse)

    end = time.perf_counter()
    
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return accessible_count, accessible_rolls


def star_2(inp_file: str, timeit = False) -> int:

    start = time.perf_counter()

    warehouse = [[x for x in line.strip()] for line in open(inp_file, 'r')]

    collected_rolls = []
    keep_cleaning = True

    while keep_cleaning:

        accessible_count, accessible_rolls = clean_area(warehouse)

        if accessible_count == 0:
            keep_cleaning = False
        else:
            collected_rolls.extend(accessible_rolls)
            for roll in accessible_rolls:
                n, m = roll
                warehouse[n][m] = '.'
    
    end = time.perf_counter()
    
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return len(collected_rolls), collected_rolls

if __name__ == "__main__":
    print(f"Star 1: {star_1('input.txt', timeit=True)[0]}")
    print(f"Star 2: {star_2('input.txt', timeit=True)[0]}")