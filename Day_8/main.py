# AOC 2025 - day 8

from math import sqrt, prod
import time


def star(inp_file: str, connections: int, timeit = False):

    start = time.perf_counter()

    junction_boxes = []
    box_in_circut = {}
    distances = {}

    with open(inp_file, 'r') as f:
        for n, line in enumerate(f.readlines()):
            curr_box = tuple([int(i) for i in line.strip().split(',')])
            junction_boxes.append(curr_box)
            box_in_circut[curr_box] = -1

            if n > 0:

                for box in junction_boxes:

                    if curr_box != box:

                        distances[(box, curr_box)] = sqrt((box[0]-curr_box[0])**2 + (box[1]-curr_box[1])**2 + (box[2]-curr_box[2])**2)


    distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}

    circuts = []
    in_circuts = set()

    for n, item in enumerate(distances.items()):

        if n == 0:

            circuts.append(list(item[0]))
            box_in_circut[item[0][0]] = 0
            box_in_circut[item[0][1]] = 0

            in_circuts.add(item[0][0])
            in_circuts.add(item[0][1])

        else:

            b1, b2 = box_in_circut[item[0][0]], box_in_circut[item[0][1]]

            if b1 > -1 and b2 > -1 and b1 == b2:
                next
            elif b1 > -1 and b2 > -1:

                if b1 < b2:

                    for box in circuts[b2]:
                        box_in_circut[box] = b1

                    circuts[b1].extend(circuts[b2])
                    circuts[b2] = []

                else:
                    for box in circuts[b1]:
                        box_in_circut[box] = b2

                    circuts[b2].extend(circuts[b1])
                    circuts[b1] = []

            elif b1 > b2:

                box_in_circut[item[0][1]] = b1
                circuts[b1].append(item[0][1])
                in_circuts.add(item[0][1])
                
            elif b1 < b2:

                box_in_circut[item[0][0]] = b2
                circuts[b2].append(item[0][0])
                in_circuts.add(item[0][0])

            else:

                circuts.append([item[0][0], item[0][1]])
                box_in_circut[item[0][0]] = len(circuts) -1
                box_in_circut[item[0][1]] = len(circuts) -1
                in_circuts.add(item[0][0])
                in_circuts.add(item[0][1])

        if len(in_circuts) == len(junction_boxes):

            end = time.perf_counter()
            if timeit:
                print(f'Execution time: {end - start:.4f} seconds')

            return item[0][0][0] * item[0][1][0]

        if n == connections - 1:
            break

    cir_lengths = [len(x) for x in circuts]
    cir_lengths.sort(reverse=True)

    end = time.perf_counter()
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return prod(cir_lengths[:3])
                

if __name__ == '__main__':
    print(f"Star 1: {star('input.txt', 1000, True)}") # 1.9 seconds ;_;
    print(f"Star 2: {star('input.txt', 99999, True)}") # 1.8 seconds ;_;