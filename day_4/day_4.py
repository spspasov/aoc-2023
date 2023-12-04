def aoc_3():
    with open('input_4.txt') as file:
        cards: list[str] = file.readlines()
        result: int = 0

        for card in cards:
            card = card.strip()
            nums = card.split(':')[-1]
            winning_nums = nums.split('|')[0].split(' ')
            my_nums = list(dict.fromkeys(nums.split('|')[-1].split(' ')))

            c_win_nums = 0
            game_result = 0

            for cur_my in my_nums:
                if not cur_my.isdigit():
                    continue

                for cur_win in winning_nums:
                    if cur_my == cur_win:
                        if c_win_nums == 0:
                            game_result += 1
                            c_win_nums += 1
                            continue
                        game_result *= 2

            result += game_result

        print(result)
        file.close()


if __name__ == '__main__':
    aoc_3()
