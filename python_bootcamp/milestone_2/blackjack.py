import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp        

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand():

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("how many chips would you like to bet? "))
        except ValueError:
            print("sorry please enter an integer")
        else:
            if chips.bet > chips.total:
                print(f"sorry, you dont have enough chips, you have {chips.total}")
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:

        x = input("hit or stand? h or s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('player stands dealer\'r turn')
            playing = False
        else:
            print('sorry, i didnt understand, please enter h or s')
            continue
        break

def show_some(player, dealer):
    print('\ndealer\'s hand: ')
    print('first card hidden!')
    print(dealer.cards[1])

    print('\nplayer\'s hand')
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print('\ndealer\'s hand')
    for card in dealer.cards:
        print(card)
    print(f'value pf dealers hand is: {dealer.value}')

    print('\nplayer\'s hand')
    for card in player.cards:
        print(card)

    print(f'value pf dealers hand is: {player.value}')

def player_busts(player, dealer, chips):
    print('bust player')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('player wins')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('bust dealer, player wins')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('dealer wins')
    chips.lose_bet()

def push(player, dealer):
    print('dealer and player tie! PUSH')

while True:

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)
    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        print(f'\nplayer total chips are at: {player_chips.total}')

        new_game = input("would you like to play another hand? y or n")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print('thanks for playing')
            break
