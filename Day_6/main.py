# AOC 2025 day 6

import time
from math import prod

def star_1(inp_file: str, timeit = False):
    start = time.perf_counter()

    inputs = []

    with open(inp_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            inputs.append([int(x) if isinstance(x, str) and x.isdigit() else x for x in line.strip().split()])

    grand_total = 0
    for n, sum_or_prod in enumerate(inputs[-1]):

        if sum_or_prod == '*':
            grand_total += prod([x[n] for x in inputs[:-1]])
        elif sum_or_prod == '+':
            grand_total += sum([x[n] for x in inputs[:-1]])

    end = time.perf_counter()
    
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return grand_total

def star_2(inp_file: str, timeit = False):
    start = time.perf_counter()

    inputs = []

    with open(inp_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            inputs.append(line.strip('\n')[::-1])

    grand_total = 0

    curr_vals = []
    for n, sum_or_prod in enumerate(inputs[-1]):

        curr_val = ''.join([x[n] for x in inputs[:-1]]).strip()

        if sum_or_prod == ' ' and curr_val == '':
            next
        elif sum_or_prod == ' ':
            curr_vals.append(int(curr_val))
            continue

        elif sum_or_prod == '*':
            curr_vals.append(int(curr_val))
            grand_total += prod(curr_vals)
            curr_vals = []

        elif inputs[-1][n] == '+':
            curr_vals.append(int(curr_val))
            grand_total += sum(curr_vals)
            curr_vals = []

    end = time.perf_counter()
    
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return grand_total


if __name__ == "__main__":
    print(f"Star 1: {star_1('input.txt', True)}")
    print(f"Star 2: {star_2('input.txt', True)}")
