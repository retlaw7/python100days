import random

dealer_hand = []
player_hand = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(p_hand, d_hand):
    p_hand.clear()
    d_hand.clear()
    d_hand.append(random.choice(cards))
    d_hand.append(random.choice(cards))
    p_hand.append(random.choice(cards))
    p_hand.append(random.choice(cards))

def deal_card(hand):
    card = random.choice(cards)
    print(f"Card drawn: {card}")
    hand.append(card)

def calc_hand(hand):
    value = sum(hand)
    pos = 0
    if 11 in hand and value > 21:
        for card in hand:
            if card == 11:
                hand[pos] = 1
            pos += 1
    value = sum(hand)
    return value

def blackjackCheck(run):
    if sum(player_hand) == 21:
        print("You have blackjack!")
        run = False
    return run

def winCheck(value_p, value_d, run):
    if value_p > 21:
        print("Busted!")
        run = False
    else:
        if sum(player_hand) == 21:
            print("You have blackjack!")
        elif value_p > value_d:
            print("You win!")
        elif sum(dealer_hand) == 21 or value_p < value_d:
            print("You lose!")
    return run

def bustCheck(hand, run):
    if sum(hand) > 21:
        print("You busted!")
        run = False
    return run
def dealerBustCheck(hand, run):
    if sum(hand) > 21:
        print("Dealer busted!")
        run = False
    return run

def main():
    # let game run
    run = True
    # let hand run
    playing = False
    while run:
        choiceG = input("Do you want to play?")
        if choiceG == "y":
            playing = True
            deal_cards(player_hand, dealer_hand)
            print(f"Your hand: {player_hand}")
            print(f"Dealer hand: {dealer_hand[0]}")
        else:
            print("have a good one!")
            break
        while playing:
            playing = blackjackCheck(playing)
            dealer_value = calc_hand(dealer_hand)
            player_value = calc_hand(player_hand)
            choiceHS = input("Do you want to draw or stand?")
            if choiceHS == "d":
                deal_card(player_hand)
                print(player_hand)
                playing = bustCheck(player_hand, playing)
                playing = blackjackCheck(playing)
            elif choiceHS == "s":
                print(f"Dealer's hand: {dealer_hand}")
                while sum(dealer_hand) < 17:
                    deal_card(dealer_hand)
                playing = dealerBustCheck(dealer_hand, playing)
                playing = winCheck(player_value, dealer_value, playing)

if __name__ == '__main__':
    main()