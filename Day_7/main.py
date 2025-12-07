# AOC 2025 day 7

import re 
import time 

def star_1(inp_file: str, timeit = False):

    start = time.perf_counter()
    all_splitters = set()

    with open(inp_file, 'r') as f:
        lines = f.readlines()
        beams = set()
        for n, line in enumerate(lines):

            if n == 0:
                beams.add(line.find('S'))

            elif line.find('^') != -1:

                splitters = [m.start() for m in re.finditer(r'\^', line)]

                for splitter in splitters:

                    if splitter in beams:

                        beams.remove(splitter)
                        all_splitters.add((n, splitter))
                        beams.add(splitter - 1)
                        beams.add(splitter + 1)

    end = time.perf_counter()
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return len(all_splitters)

def traverse(inp_array: list, init_node: tuple, nodes: dict) -> int:
    
    for n, line in enumerate(inp_array[init_node[0]+1:]):

        if line[init_node[1]] == '^':

            curr_node = (init_node[0]+n+1, init_node[1])

            try:
                val = nodes[curr_node]
                return val
            
            except:
                
                nodes[curr_node] = 0

                nodes[curr_node] += traverse(inp_array, (curr_node[0], curr_node[1] -1), nodes)
                nodes[curr_node] += traverse(inp_array, (curr_node[0], curr_node[1] + 1), nodes)

                return nodes[curr_node]

    return 1

def star_2(inp_file: str, timeit = False):
    
    start = time.perf_counter()

    inp_array = [line.strip() for line in open(inp_file, 'r')]

    curr_node = (0, inp_array[0].find('S'))
    nodes = {}

    total_timelines = 0
    total_timelines += traverse(inp_array, curr_node, nodes)

    end = time.perf_counter()
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return total_timelines


if __name__ == '__main__':
    print(star_1('input.txt', timeit=True))
    print(star_2('input.txt', timeit=True))
