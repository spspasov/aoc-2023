def aoc_6():
    with open('input.txt') as file:
        lines = file.readlines()

        times = lines[0].split(':')[1].strip().split(' ')
        records = lines[1].split(':')[1].strip().split(' ')
        distances = []

        for time in times:
            race = []

            if not time:
                continue

            for duration in range(int(time.strip())+1):
                distance = duration * (int(time) - duration)
                race.append(distance)

            distances.append(race)

        product = 1

        for i, record in enumerate(records):
            sum = 0
            for distance in distances[i]:
                if distance > int(record.strip()):
                    sum += 1

            product *= sum

        print(product)


if __name__ == '__main__':
    aoc_6()
