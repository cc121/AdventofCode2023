from collections import Counter


cards = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'J': 9,
    'T': 8,
    '9': 7,
    '8': 6,
    '7': 5,
    '6': 4,
    '5': 3,
    '4': 2,
    '3': 1,
    '2': 0,
}


jcards = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0,
}


def convert_hand_to_number(hand, card_map, base=13):
    numeric_hand = 0
    for i, card in enumerate(hand[::-1]):
        numeric_hand += (base ** i) * card_map[card]
    return numeric_hand


def sort_hand(hands, card_map):
    def card_conversion(hand):
        return convert_hand_to_number(hand, card_map)

    return sorted(hands, key=card_conversion, reverse=True)


def sort_and_score(hands, n, bids, card_map):
    sorted_hand = sort_hand(hands, card_map)

    score = 0
    for hand in sorted_hand:
        score += n * bids[hand]
        n -= 1
    return score, n


def part1(input_list):
    input_list = input_list.split('\n')

    hands = []
    bids = {}
    for row in input_list:
        hand, bid = row.split(' ')
        hands.append(hand)
        bids[hand] = int(bid)

    fvoak = []
    foak = []
    fh = []
    toak = []
    tp = []
    op = []
    hc = []
    for hand in hands:
        c = Counter(hand)
        if any([val == 5 for key, val in c.items()]):
            # print(f"Hand {hand} had five of a kind!")
            fvoak.append(hand)
        elif any([val == 4 for key, val in c.items()]):
            # print(f"Hand {hand} had four of a kind!")
            foak.append(hand)
        elif any([val == 3 for key, val in c.items()]):
            if any([val == 2 for key, val in c.items()]):
                # print(f"Hand {hand} had full house!")
                fh.append(hand)
            else:
                # print(f"Hand {hand} had three of a kind!")
                toak.append(hand)
        elif any([val == 2 for key, val in c.items()]):
            if len(set([key for key, val in c.items() if val == 2])) == 2:
                # print(f"Hand {hand} had two pair!")
                tp.append(hand)
            else:
                # print(f"Hand {hand} had one pair!")
                op.append(hand)
        else:
            # print(f"Hand {hand} has a high card!")
            hc.append(hand)

    scores = []
    n = len(hands)

    score, n = sort_and_score(fvoak, n, bids, cards)
    scores.append(score)

    score, n = sort_and_score(foak, n, bids, cards)
    scores.append(score)

    score, n = sort_and_score(fh, n, bids, cards)
    scores.append(score)

    score, n = sort_and_score(toak, n, bids, cards)
    scores.append(score)

    score, n = sort_and_score(tp, n, bids, cards)
    scores.append(score)

    score, n = sort_and_score(op, n, bids, cards)
    scores.append(score)

    score, n = sort_and_score(hc, n, bids, cards)
    scores.append(score)

    return sum(scores)


def part2(input_list):
    input_list = input_list.split('\n')

    hands = []
    bids = {}
    for row in input_list:
        hand, bid = row.split(' ')
        hands.append(hand)
        bids[hand] = int(bid)

    fvoak = []
    foak = []
    fh = []
    toak = []
    tp = []
    op = []
    hc = []
    ranking_hands = {
        7: fvoak,
        6: foak,
        5: fh,
        4: toak,
        3: tp,
        2: op,
        1: hc

    }
    for hand in hands:
        best_score = 0
        for key in jcards.keys():
            if key == 'J':
                continue
            new_hand = hand.replace(key, 'J')

            c = Counter(new_hand)
            if any([val == 5 for key, val in c.items()]):
                # print(f"Hand {hand} had five of a kind!")
                score = 7
            elif any([val == 4 for key, val in c.items()]):
                # print(f"Hand {hand} had four of a kind!")
                score = 6
            elif any([val == 3 for key, val in c.items()]):
                if any([val == 2 for key, val in c.items()]):
                    # print(f"Hand {hand} had full house!")
                    score = 5
                else:
                    # print(f"Hand {hand} had three of a kind!")
                    score = 4
            elif any([val == 2 for key, val in c.items()]):
                if len(set([key for key, val in c.items() if val == 2])) == 2:
                    # print(f"Hand {hand} had two pair!")
                    score = 3
                else:
                    # print(f"Hand {hand} had one pair!")
                    score = 2
            else:
                # print(f"Hand {hand} has a high card!")
                score = 1

            if score > best_score:
                best_score = score
        ranking_hands[best_score].append(hand)

    scores = []
    n = len(hands)

    score, n = sort_and_score(fvoak, n, bids, jcards)
    scores.append(score)

    score, n = sort_and_score(foak, n, bids, jcards)
    scores.append(score)

    score, n = sort_and_score(fh, n, bids, jcards)
    scores.append(score)

    score, n = sort_and_score(toak, n, bids, jcards)
    scores.append(score)

    score, n = sort_and_score(tp, n, bids, jcards)
    scores.append(score)

    score, n = sort_and_score(op, n, bids, jcards)
    scores.append(score)

    score, n = sort_and_score(hc, n, bids, jcards)
    scores.append(score)

    return sum(scores)

