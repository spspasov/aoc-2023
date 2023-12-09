import math
from functools import reduce

import pandas as pd
def aoc_8():
    with open('locations.txt') as file:
        lines = file.readlines()
        with open('directions.txt') as file2:
            directions = file2.readlines()[0].strip()
            file2.close()
        locations = pd.read_csv('locations.txt', sep=" = ", engine='python').iloc[:, :1].values.tolist()

        DIRECTIONS = {
            'L': 0,
            'R': 1,
        }

        locs_and_dirs = {}
        for line in lines:
            data = line.split(' = ')
            line_loc = data[0]
            line_dir = data[1].strip()[1:-1].split(', ')
            locs_and_dirs[line_loc] = line_dir

        starting_locations = []

        del(locs_and_dirs['row1'])

        for location in locations:
            if location[0].endswith('A'):
                starting_locations.append(location[0])

        count = 0
        i = 0
        all_count = []

        for loc in starting_locations:
            while True:
                if i == len(directions):
                    i = 0
                    continue
                count += 1

                dir = directions[i]
                next = locs_and_dirs[loc][DIRECTIONS[dir]]
                loc = next

                if next.endswith('Z'):
                    all_count.append(count)
                    count = 0
                    i = 0
                    break

                i += 1

        # find the lcm for all the separate paths
        lcm = 1
        for i in all_count:
            lcm = lcm * i // math.gcd(lcm, i)
        print(lcm)

        file.close()


aoc_8()