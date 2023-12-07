maps = {
    'seeds': [],
    'seed-to-soil map': [],
    'soil-to-fertilizer map': [],
    'fertilizer-to-water map': [],
    'water-to-light map': [],
    'light-to-temperature map': [],
    'temperature-to-humidity map': [],
    'humidity-to-location map': [],
}


def aoc_5():
    with open('input.txt') as file:
        lines = file.readlines()

        for line in lines:
            if not line[0].isdigit() and not line.isspace():
                i = line.strip()[:-1]
                continue
            if line == '\n':
                continue

            maps[i].append(line.strip())

        seeds = maps['seeds'][0].split(' ')
        seeds = ' '.join(seeds[:2]), ' '.join(seeds[2:])
        seed_ranges = []

        for seed_range in seeds:
            start_seed_range = seed_range.split(' ')
            seed_ranges.append(range(int(start_seed_range[0]), int(start_seed_range[0]) + int(start_seed_range[1])))

        del maps['seeds']

        prev_source = seed_ranges
        next_source = []

        for map_val in maps:

            print(map_val)

            for prev in prev_source:
                if isinstance(prev, range):
                    print(prev)
                    for prev_from_range in prev:
                        try:
                            for row in maps[map_val]:
                                nums = row.split(' ')
                                dest = int(nums[0])
                                source = int(nums[1])
                                range_length = int(nums[2])

                                if int(prev_from_range) in range(source, source + range_length):
                                    next_source.append(int(prev_from_range) + dest - source)
                                    # we want to break out of the two loops
                                    raise Exception('Number Found')
                        except Exception:
                            continue

                        # if we reach here, it means the number is not in any of the ranges
                        next_source.append((int(prev_from_range)))
                else:
                    if not str(prev).isdigit():
                        continue

                    try:
                        for row in maps[map_val]:
                            nums = row.split(' ')
                            dest = int(nums[0])
                            source = int(nums[1])
                            range_length = int(nums[2])

                            if int(prev) in range(source, source + range_length):
                                next_source.append(int(prev) + dest - source)
                                # we want to break out of the two loops
                                raise Exception('Number Found')
                    except Exception:
                        continue

                    # if we reach here, it means the number is not in any of the ranges
                    next_source.append((int(prev)))

            # we've checked all the numbers, continue to next map
            prev_source = next_source
            next_source = []

        print(min(prev_source))


if __name__ == '__main__':
    aoc_5()
