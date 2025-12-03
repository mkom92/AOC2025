# AOC 2025 day 3

import time

def star_1(inp_file: str, timeit = False) -> int:

    start = time.perf_counter()
    inp_array = [line.strip() for line in open(inp_file, 'r')]

    joltage = 0
    for banks in inp_array:

        batteries = [int(x) for x in banks]

        first_digit = max(batteries[0:-1])
        if batteries[-1] > first_digit:
            second_digit = batteries[-1]
        elif batteries.count(first_digit) > 1:
            second_digit = first_digit
        else:
            second_digit = max(batteries[batteries.index(first_digit)+1:])

        joltage += int(str(first_digit) + str(second_digit))
    
    end = time.perf_counter()
    
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')
    
    return joltage


def star_2(inp_file: str, timeit = False) -> int:

    start = time.perf_counter()
    inp_array = [line.strip() for line in open(inp_file, 'r')]

    joltage = 0
    for banks in inp_array:

        batteries = [int(x) for x in banks]
        turned_on = [0 for _ in range(12)]
        curr_battery_index = 0

        for n,_ in enumerate(turned_on):

            if n == 0:
                turned_on[0] = max(batteries[0:-11])
            elif n == 11:
                turned_on[n] = max(batteries[curr_battery_index:])
            else:
                turned_on[n] = max(batteries[curr_battery_index:-11+n])
            
            if n < 11:
                curr_battery_index = batteries[curr_battery_index:-11+n].index(turned_on[n]) + curr_battery_index + 1
        
        joltage += int(''.join([str(x) for x in turned_on]))
    
    end = time.perf_counter()
    
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')
    
    return joltage

if __name__ == "__main__":
    print(f"Star 1: {star_1('input.txt', True)}")
    print(f"Star 2: {star_2('input.txt', True)}")