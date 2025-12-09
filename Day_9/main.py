# AOC 2025 day 9

import time



def star_1(inp_file: str, timeit = False):

    start = time.perf_counter()

    red_tiles = []
    areas = {}

    with open(inp_file, 'r') as f:
        for n, line in enumerate(f.readlines()):
            curr_tile = tuple([int(i) for i in line.strip().split(',')])
            red_tiles.append(curr_tile)

            if n > 0:

                for tile in red_tiles:

                    if curr_tile != tile:

                        areas[(tile, curr_tile)] = (abs(tile[0]-curr_tile[0])+1) * (abs(tile[1]-curr_tile[1])+1)

    areas = {k: v for k, v in sorted(areas.items(), key=lambda item: item[1], reverse=True)}

    end = time.perf_counter()
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return next(iter(areas.items()))

# print(star_1('input.txt', True))

# Ray casting algorithm
# Check if the other corners of the potential rectangle are within the polygon and then calculate their area
# The rays will be casting from left to right, so I only need these edges - i.e. y_1 = y_2


# Step 1 - collect corners and sides

sides = []
corners = []

with open('test.txt', 'r') as f:
    for n, line in enumerate(f.readlines()):
        curr_point = tuple([int(i) for i in line.strip().split(',')])

        corners.append(curr_point)
        
        if n == 0:
            next
        elif corners[n-1][1] == curr_point[1]:

            if corners[n-1][0] < curr_point[0]:
                sides.append([corners[n-1], curr_point])
            else:
                sides.append([curr_point, corners[n-1]])

    if curr_point[1] == corners[0][1]:
        
            if corners[0][0] < curr_point[0]:
                sides.append([corners[0], curr_point])
            else:
                sides.append([curr_point, corners[0]])

# The sides are horizontal
sides = sorted(sides, key=lambda x: x[0][1])

def ray_casting(point: tuple, sides: list) -> bool:

    crossed_walls = 0
    r_corner, l_corner = 0, 0

    in_out = False

    for side in sides:

        if point[1] < side[0][1]:
            break

        elif (point == side[0] or point == side[1]):
            return True
        
        elif point[0] < side[0][0] or point[0] > side[1][0]:
            next

        elif point[0] == side[0][0]:

            if r_corner == 1:
                r_corner = 0
            else:
                l_corner = (l_corner - 1)**2
                in_out = not in_out

        elif point[0] == side[1][0]:
            
            if r_corner == 1:
                r_corner = (r_corner - 0)
                in_out = not in_out
            elif l_corner == 1:
                l_corner = 0

        else:
            in_out = not in_out
            crossed_walls += 1

    return in_out

areas = {}
for n, corner in enumerate(corners):

    if n == 0:
        next
    
    else:

        for other_corner in corners[:n]:

            point_1, point_2 = (corner[0], other_corner[1]), (other_corner[0], corner[1])

            # Are the 2 new corners inside the polygon
            test_1 = ray_casting(point_1, sides)
            test_2 = ray_casting(point_2, sides)

            # if (other_corner, corner) == ((9, 5), (2, 3)):
            #     print(f"Known: ({other_corner}, {corner}), tested: {point_1}: {test_1}, {point_2}: {test_2}")

            if test_1 and test_2:

                areas[(other_corner, corner)] = (abs(other_corner[0]-corner[0])+1) * (abs(other_corner[1]-corner[1])+1)
        
areas = {k: v for k, v in sorted(areas.items(), key=lambda item: item[1], reverse=True)}

# print(areas)

print(next(iter(areas.items())))