def aoc_4():
    with open('input_4.txt') as file:
        cards: list[str] = file.readlines()
        won_cards: dict = {}

        for card in cards:
            card = card.strip()
            nums = card.split(':')[-1]
            winning_nums = nums.split('|')[0].split(' ')
            game_id = card.split(':')[0].split(' ')[-1]
            my_nums = list(dict.fromkeys(nums.split('|')[-1].split(' ')))

            try:
                try:
                    iterations = won_cards[int(game_id)] + 1
                except KeyError as error:
                    iterations = 1

                for i in range(0, iterations):

                    cards_won = 0

                    for cur_my in my_nums:
                        if not cur_my.isdigit():
                            continue

                        for cur_win in winning_nums:
                            if not cur_my.isdigit():
                                continue

                            if cur_my == cur_win:
                                cards_won += 1

                    for i in range(int(game_id)+1, int(game_id)+cards_won+1):
                        try:
                            won_cards[i] = won_cards[i] + 1
                        except KeyError as error:
                            won_cards[i] = 1
            except KeyError as error:
                # game over, we calculate total scores
                pass

        print(won_cards)
        sum = 0
        for card_game in won_cards:
            sum += won_cards[card_game]
        file.close()
        print(sum + len(cards))


if __name__ == '__main__':
    aoc_4()
