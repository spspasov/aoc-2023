import math

import pandas as pd
def aoc_8():
    with open('locations-test.txt') as file:
        lines = file.readlines()
        with open('directions-test.txt') as file2:
            directions = file2.readlines()[0].strip()
            file2.close()
        locations = pd.read_csv('locations-test.txt', sep=" = ", engine='python').iloc[:, :1].values.tolist()

        DIRECTIONS = {
            'L': 0,
            'R': 1,
        }

        starting_locations = []
        ending_locations = []

        locs_and_dirs = {}
        for line in lines:
            data = line.split(' = ')
            line_loc = data[0]
            line_dir = data[1].strip()[1:-1].split(', ')
            locs_and_dirs[line_loc] = line_dir

        del(locs_and_dirs['row1'])

        for location in locations:
            if location[0].endswith('A'):
                starting_locations.append(location[0])

        count = 0
        i = 0

        while True:
            if i == len(directions):
                i = 0
                continue

            count += 1

            for loc in starting_locations:
                dir = directions[i]
                next = locs_and_dirs[loc][DIRECTIONS[dir]]

                ending_locations.append(next)

            starting_locations = ending_locations
            ending_locations = []

            # check if all locations end in Z
            result = [x for x in starting_locations if not x.endswith('Z')]

            # all entries end in Z
            if not result:
                break

            i += 1

        print(count)
        print(abs(2 * 3) // math.gcd(1, 2, 3))
        file.close()


if __name__ == '__main__':
    aoc_8()
