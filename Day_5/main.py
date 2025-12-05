# AOC 2025 day 5

import time

def merge_ranges(ranges):

    # Sort by start
    ranges.sort(key=lambda x: x[0])
    merged = []
    cur_s, cur_e = ranges[0]
    for s, e in ranges[1:]:
        # Merge when overlapping or touching (inclusive)
        if s <= cur_e:
            cur_e = max(cur_e, e)
        else:
            merged.append((cur_s, cur_e))
            cur_s, cur_e = s, e
    merged.append((cur_s, cur_e))
    return merged

def stars(inp_file: str, timeit = False):

    start = time.perf_counter()

    fresh_ingredients_ranges, ingredients = [], []

    ranges = True
    for line in open(inp_file, 'r'):
        line = line.strip()
        if line == '':
            ranges = False
            continue

        if ranges:
            fresh_ingredients_ranges.append(tuple(map(int, line.split('-'))))
        else:
            ingredients.append(int(line))

    fresh_ingredients_ranges = merge_ranges(fresh_ingredients_ranges)
    ingredients.sort()

    spoiled_ingredients = []

    ingredient_pos = 0
    for m, range in enumerate(fresh_ingredients_ranges):

        x,y = range

        for n, ingredient in enumerate(ingredients[ingredient_pos:]):
            if ingredient > y:
                ingredient_pos += n

                if m == len(fresh_ingredients_ranges) - 1:
                    spoiled_ingredients.extend(ingredients[ingredient_pos:])
                break

            if ingredient < x:
                spoiled_ingredients.append(ingredient)

    fresh_count = len(ingredients) - len(spoiled_ingredients)
    possible_fresh_count = sum([y - x + 1 for x,y in fresh_ingredients_ranges])

    end = time.perf_counter()
    
    if timeit:
        print(f'Execution time: {end - start:.4f} seconds')

    return fresh_count, possible_fresh_count

if __name__ == "__main__":

    inp_file = 'input.txt'
    fresh_count, possible_fresh_count = stars(inp_file, timeit=True)

    print(f'Fresh ingredients: {fresh_count}')
    print(f'Possible fresh ingredients: {possible_fresh_count}')