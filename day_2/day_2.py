import os

rules: dict = {
    'red': 0,
    'green': 0,
    'blue': 0,
}

def aoc_2():
    with open('input_2.txt') as file:
        games: list[str] = file.readlines()
        result: int = 0

        for draws in games:
            draws: list[str] = draws.split(':')[1].split(';')

            for draw in draws:
                cubes: list[str] = draw.split(',')
                for cube in cubes:
                    cube_amount, color = cube.strip().split(' ')
                    if rules[color] < int(cube_amount):
                        rules[color] = int(cube_amount)

            result += rules['red'] * rules['green'] * rules['blue']

            # reset the rules
            rules['red'] = 0
            rules['green'] = 0
            rules['blue'] = 0

        print(result)
        file.close()


if __name__ == '__main__':
    aoc_2()
