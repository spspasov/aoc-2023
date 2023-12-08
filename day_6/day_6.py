def aoc_6():
    with open('input.txt') as file:
        lines = file.readlines()
        time = int(lines[0].split(':')[1].strip().split(' ')[0])
        record = lines[1].split(':')[1].strip().split(' ')[0]

        for duration in range(time):
            distance = duration * (time - duration)

            if distance > int(record):
                print(time - duration*2 + 1)
                return


if __name__ == '__main__':
    aoc_6()