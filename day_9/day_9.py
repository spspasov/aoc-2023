def aoc_6():
    diff_lists = []
    with open('input.txt') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split(' ')
            check_diffs(line)
            new_list = [line] + diffs.copy()
            diff_lists.append(new_list)
            diffs.clear()

    count = 0
    for diff_list in diff_lists:
        for l in diff_list:
            l.reverse()

        diff_list.reverse()
        for i, rlist in enumerate(diff_list):
            if i == len(diff_list)-1:
                count += diff_list[-1][-1]
                print(diff_list)
                break
            diff_list[i+1].append(int(diff_list[i+1][-1]) - int(rlist[-1]))
    print(count)

diffs = []
def check_diffs(seq):
    cur_diff = []
    for i, num in enumerate(seq):
        if i == len(seq) - 1:
            continue
        cur_diff.append(int(seq[i + 1]) - int(num))

    diffs.append(cur_diff)

    if all(element == 0 for element in cur_diff):
        cur_diff.append(0)
        return

    check_diffs(cur_diff)

aoc_6()