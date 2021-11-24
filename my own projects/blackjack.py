#not functional yet

import random
#generate deck
deck = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "T♠", "J♠", "Q♠", "K♠",
        "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "T♥", "J♥", "Q♥", "K♥",
        "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "T♦", "J♦", "Q♦", "K♦",
        "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "T♣", "J♣", "Q♣", "K♣"]

balance = 50

player_hand = []
dealer_hand = []
player_value = 0
dealer_value = 0

#deal cards to start
def deal_cards():
    count = 0
    while count < 4:
        if count % 2:
            draw = random.randint(0, len(deck))
            draw -= 1
            player_hand.append(deck[draw])
            deck.pop(draw)
        else:
            draw = random.randint(0, len(deck))
            draw -= 1
            dealer_hand.append(deck[draw])
            deck.pop(draw)
        count += 1

#draw single card
def draw_card(hand):
    draw = random.randint(0, len(deck))
    draw -= 1
    hand.append(deck[draw])
    print(f"Card drawn: {deck[draw]}")
    deck.pop(draw)

#calculate card value
def calc_value(hand, value):
    new_hand = []
    for card in hand:
        #strip card symbol
        card_value = card.replace("♠", "").replace("♥", "").replace("♦", "").replace("♣", "")
        new_hand.append(card_value)
    for card in new_hand:
        # check if it's a number or a letter
        try:
            value += int(card)
        except:
            #ACE check
            if card == "A":
                #checks for if your hand size is at 2 and if you have a TJQK next to your A
                if len(new_hand) == 2 and "T" in new_hand or "J" in new_hand or "Q" in new_hand or "K" in new_hand:
                    value += 11
                #if you already have 10 and you draw an ACE
                elif value == 10:
                    value += 11
                #otherwise just make it count as 1 to keep it as the lowest value
                else:
                    value += 1
            elif card == "T" or "J" or "Q" or "K":
                value += 10
    return value

#check for blackjack
def blackjack_check(value):
    if value == 21:
        print("Blackjack!")
    elif value > 21:
        print("Busted")

def main():
    deal_cards()
    print(f"Player hand: {player_hand[0]} {player_hand[1]}")
    print(f"Dealer hand: {dealer_hand[0]}")

    value_p = calc_value(player_hand, player_value)

    #check blackjack player
    blackjack_check(value_p)
    while value_p < 21:
        print(f"Your total card value is: {value_p}")
        choice = input("Do you want to hit 'h' or stand 's'?")
        #hit
        if choice == "h":
            draw_card(player_hand)
            value_p = calc_value(player_hand, player_value)
            blackjack_check(value_p)
        #stand
        elif choice == "s":
            run = True
            value_d = calc_value(dealer_hand, dealer_value)
            print(f"Dealer hand: {dealer_hand[0]} {dealer_hand[1]}")
            while run:
                if value_d == 21:
                    print(f"Dealer value: {value_d}")
                    print("Blackjack for the dealer")
                    run = False
                elif value_d < 17:
                    draw_card(dealer_hand)
                    value_d = calc_value(dealer_hand, dealer_value)
                    print(f"Dealer value: {value_d}")
                elif value_d > 21:
                    print(f"Dealer value: {value_d}")
                    print("Dealer busted")
                    break
                else:
                    if value_d > value_p:
                        print("Dealer wins")
                        break
                    else:
                        print("You win")
                        break


        else:
            print("Wrong input, try again!")

if __name__ == '__main__':
    main()