def aoc_8():
    with open('input.txt') as file:
        lines = file.readlines()
        directions = lines[:1][0].strip()
        locations = lines[2:]
        locations_dict = {}

        DIRECTIONS = {
            'L': 0,
            'R': 1,
        }

        for location in locations:
            loc = location.split('=')
            locations_dict[loc[0].strip()] = loc[1].strip()[1:-1].replace(' ', '').split(',')

        start = 'AAA'
        current = start
        end = 'ZZZ'

        count = 0
        i = 0

        while True:
            count += 1
            dir = directions[i]
            current = locations_dict[current][DIRECTIONS[dir]]

            if current == end:
                break

            if i == len(directions) - 1:
                i = 0
                continue
            i += 1

        print(count)


if __name__ == '__main__':
    aoc_8()
