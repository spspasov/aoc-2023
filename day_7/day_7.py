import operator
def aoc_7():
    with open('input.txt') as file:
        lines = file.readlines()

        alphabet = "J23456789TQKA"
        NOTHING = 0
        PAIR = 1
        TWO_PAIR = 2
        THREE_OF_A_KIND = 3
        FULL_HOUSE = 4
        FOUR_OF_A_KIND = 5
        FIVE_OF_A_KIND = 6

        JOKER = 1
        CARDS = {
            'J': 1,
            'T': 10,
            'Q': 12,
            'K': 13,
            'A': 14,
        }

        hands = []
        bets = []
        hands_and_bets = []

        for hand_and_bet in lines:
            hand_and_bet = hand_and_bet.split(' ')

            hand = (hand_and_bet[0])
            bet = hand_and_bet[1].strip()

            hands.append(hand)
            bets.append(bet)

            hands_and_bets.append([hand, bet])


        sorted_hands = []
        high_card = []

        for hand in hands_and_bets:
            for card in hand[0]:
                if not card.isdigit():
                    high_card.append(CARDS[card])
                else:
                    high_card.append(int(card))

            sorted_hand = sorted(hand[0], key=lambda word: [alphabet.index(c) for c in word])
            sorted_hands.append([high_card, sorted_hand, hand[1]])
            high_card = []

        hand_and_high_card = []

        for hand in sorted_hands:
            matches = []
            card_counter = 1
            for i, card in enumerate(hand[1]):
                if i == 0:
                    continue

                if card == 'J':
                    continue

                if card == hand[1][i-1]:
                    # we have a match, add it
                    card_counter += 1
                else:
                    # calculate the matches
                    if card_counter == 2:
                        matches.append(PAIR)
                    if card_counter == 3:
                        matches.append(THREE_OF_A_KIND)
                    if card_counter == 4:
                        matches.append(FOUR_OF_A_KIND)
                    if card_counter == 5:
                        matches.append(FIVE_OF_A_KIND)
                    card_counter = 1

            # calculate the matches for the last card
            if card_counter == 2:
                matches.append(PAIR)
            if card_counter == 3:
                matches.append(THREE_OF_A_KIND)
            if card_counter == 4:
                matches.append(FOUR_OF_A_KIND)
            if card_counter == 5:
                matches.append(FIVE_OF_A_KIND)

            if not matches:
                matches = [NOTHING]
            hand_and_high_card.append([hand[0], matches, int(hand[2])])


        # check if we have 2 pair or full house
        for card in hand_and_high_card:
            if not card[1] or len(card[1]) < 2:
                continue

            if card[1].count(PAIR) == 2:
                match_val = TWO_PAIR
            else:
                match_val = FULL_HOUSE

            card[1] = [match_val]

        # check the Joker
        for i, card in enumerate(hand_and_high_card):
            # skip this as we don't care about Jokers here
            if card[1] == FIVE_OF_A_KIND:
                continue

            # if no Jokers, continue, obv
            if not JOKER in card[0]:
                continue

            for i in range(operator.countOf(card[0], JOKER)):
                if card[1] == [NOTHING]:
                    card[1] = [PAIR]
                    continue

                if card[1] == [PAIR]:
                    card[1] = [THREE_OF_A_KIND]
                    continue

                if card[1] == [TWO_PAIR]:
                    card[1] = [FULL_HOUSE]
                    continue

                if card[1] == [THREE_OF_A_KIND]:
                    card[1] = [FOUR_OF_A_KIND]
                    continue

                if card[1] == [FULL_HOUSE]:
                    card[1] = [FOUR_OF_A_KIND]
                    continue

                if card[1] == [FOUR_OF_A_KIND]:
                    card[1] = [FIVE_OF_A_KIND]
                    break

        # calculate scores
        sorted_list = sorted(hand_and_high_card, key=operator.itemgetter(1, 0))

        print(sorted_list)

        bets_sum = 0

        for i, final_hand in enumerate(sorted_list):
            bets_sum += final_hand[2] * (i+1)

        print(bets_sum)


if __name__ == '__main__':
    aoc_7()
