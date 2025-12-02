# AOC 2025 day 2

import time
import re

inp_array = [line.split(',') for line in open('input.txt', 'r')][0]

def star_1(inp_array, timeit = False) -> int:

    start = time.perf_counter()
    total_incorrect = 0
    for i in inp_array:
        x,y = i.split('-')

        for j in range(int(x), int(y)+1):

            if str(j)[:len(str(j))//2] == str(j)[len(str(j))//2:]:
                total_incorrect += j

    end = time.perf_counter()
    
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return total_incorrect


def is_repetition(s: str) -> bool:
    """
    This function checks if the string `s` is a repetition of a substring.
    Successfully generated with a prompt.

    Return True if the entire string `s` consists of one substring repeated at least twice.

    Uses a backreference regex: the pattern captures the smallest prefix (lazy) and
    requires it to repeat to fill the whole string.
    """
    if not isinstance(s, str):
        return False
    if len(s) < 2:
        return False
    return re.fullmatch(r"(.+?)\1+", s) is not None


def star_2(inp_array, timeit = False) -> int:

    start = time.perf_counter()
    total_incorrect = 0
    for i in inp_array:
        x,y = i.split('-')

        for j in range(int(x), int(y)+1):

            if is_repetition(str(j)):
                total_incorrect += j

    end = time.perf_counter()
    
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return total_incorrect


if __name__ == '__main__':
    print(f'Star 1: {star_1(inp_array)}')
    print(f'Star 2: {star_2(inp_array)}')