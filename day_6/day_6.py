def aoc_6():
    with open('input.txt') as file:
        lines = file.readlines()
        time = lines[0].split(':')[1].strip().split(' ')[0]
        record = lines[1].split(':')[1].strip().split(' ')[0]

        for duration in range(int(time.strip())+1):
            distance = duration * (int(time) - duration)

            if distance > int(record):
                print(int(time) - duration*2 + 1)
                return 1


if __name__ == '__main__':
    aoc_6()