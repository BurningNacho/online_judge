# A poker deck contains 52 cards - each card has a suit which is one of clubs, diamonds, hearts, or spades
# (denoted C, D, H, S in the input data). Each card also has a value which is one of 2, 3, 4, 5, 6, 7, 8, 9,
# 10, jack, queen, king, ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A). For scoring purposes, the suits
# are unordered while the values are ordered as given above, with 2 being the lowest and ace the highest
# value.
# A poker hand consists of 5 cards dealt from the deck. Poker hands are ranked by the following
# partial order from lowest to highest
# High Card. Hands which do not fit any higher category are ranked by the value of their highest card.
# If the highest cards have the same value, the hands are ranked by the next highest, and so on.
# Pair. 2 of the 5 cards in the hand have the same value. Hands which both contain a pair are ranked
# by the value of the cards forming the pair. If these values are the same, the hands are ranked by
# the values of the cards not forming the pair, in decreasing order.
# Two Pairs. The hand contains 2 different pairs. Hands which both contain 2 pairs are ranked by the
# value of their highest pair. Hands with the same highest pair are ranked by the value of their
# other pair. If these values are the same the hands are ranked by the value of the remaining card.
# Three of a Kind. Three of the cards in the hand have the same value. Hands which both contain
# three of a kind are ranked by the value of the 3 cards.
# Straight. Hand contains 5 cards with consecutive values. Hands which both contain a straight are
# ranked by their highest card.
# Flush. Hand contains 5 cards of the same suit. Hands which are both flushes are ranked using the
# rules for High Card.
# Full House. 3 cards of the same value, with the remaining 2 cards forming a pair. Ranked by the
# value of the 3 cards.
# Four of a kind. 4 cards with the same value. Ranked by the value of the 4 cards.
# Straight flush. 5 cards of the same suit with consecutive values. Ranked by the highest card in the
# hand.
# Your job is to compare several pairs of poker hands and to indicate which, if either, has a higher
# rank.
# Input
# The input file contains several lines, each containing the designation of 10 cards: the first 5 cards are
# the hand for the player named ‘Black’ and the next 5 cards are the hand for the player named ‘White’.
# Output
# For each line of input, print a line containing one of:
# Black wins.
# White wins.
# Tie.
# Sample Input
# 2H 3D 5S 9C KD                2C 3H 4S 8C AH
# 2H 4S 4C 2D 4H 2S 8S AS QS 3S
# 2H 3D 5S 9C KD 2C 3H 4S 8C KH
# 2H 3D 5S 9C KD 2D 3H 5C 9S KH
# Sample Output
# White wins.
# Black wins.
# Black wins.
# Tie.


playing_cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'B', 'J', 'Q', 'K', 'R'] ## T == B, A == R
straight_flush = 8
four_of_a_kind = 7
full_house = 6
flush = 5
straight = 4
three_of_a_kind = 3
two_pairs = 2
pair = 1
high_card = 0

def nex_card(card, i):
    return playing_cards[(playing_cards.index(card)+i) % 14] ## Rotatory

def max_rank(hand):
    numbers = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    best_hand = []
    if suits.count(suits[0]) == 5:
        if not False in [number == nex_card(numbers[0],i) for i,number in enumerate(numbers)]:
            return [straight_flush, hand[4][0]]
        best_hand = [flush, hand[4][0], hand[3][0], hand[2][0], hand[1][0], hand[0][0]]

    if numbers.count(numbers[2]) == 4:
        return [four_of_a_kind, hand[2][0]]

    if not False in [number == nex_card(numbers[0],i) for i,number in enumerate(numbers)]:
        return [straight, hand[4][0]]

    if numbers.count(numbers[1]) == 2 or numbers.count(numbers[3]) == 2:
        if numbers.count(numbers[2]) == 3:
            return [full_house, hand[2][0]]
        if best_hand:
            return best_hand
        if numbers.count(numbers[1]) == numbers.count(numbers[3]):
            best_hand = [two_pairs, max(numbers[1], numbers[3]), min(numbers[1], numbers[3])]
            best_hand.append(''.join(reversed(numbers)).replace(best_hand[1],'').replace(best_hand[2],''))
            return best_hand
        if numbers.count(numbers[1]) == 2:
            best_hand = [pair, numbers[1]]
            return best_hand + [number for number in reversed(numbers) if number != numbers[1]]
        else:
            best_hand = [pair, numbers[3]]
            return best_hand + [number for number in reversed(numbers) if number != numbers[3]]

    if numbers.count(numbers[2]) == 3:
        best_hand = [three_of_a_kind, numbers[2]]
        return best_hand + [number for number in reversed(numbers) if number != numbers[3]]
    if best_hand:
        return best_hand
    return [high_card, list(reversed(numbers))]


def pick_winner(W_hand, B_hand):
    W_hand_max = max_rank(W_hand)
    B_hand_max = max_rank(B_hand)
    if W_hand_max[0] > B_hand_max[0]:
        return 'Black wins.'
    if B_hand_max[0] > W_hand_max[0]:
        return 'White wins.'
    for i, j in zip(W_hand_max[1:], B_hand_max[1:]):
        if str(i) > str(j):
            return 'Black wins.'
        if str(i) < str(j):
            return 'White wins.'
    return 'Tie.'

if __name__ == '__main__':

    poker_game = []
    hands = input()
    while hands:
        if not(hands == ''):
            poker_game.append([[card[0],card[1]] for card in hands.replace('A', 'Z').replace('T','B').replace('K','S').strip().split()])
        try:
            hands = input()
        except:
            hands = ''
    for hands in poker_game:
        try:
            print(pick_winner(sorted(hands[:5]), sorted(hands[5:])))
        except:
            pass
