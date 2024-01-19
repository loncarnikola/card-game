import random
# Ranks of the cards
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
          'Ten', 'Jack', 'Queen', 'King', 'Ace']
# All card suits
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# Dictionary for giving value to the rank
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Ace': 11,'Jack': 10, 'Queen': 10, 'King': 10}

class Card():
    # Create an instance of a card
    def __init__(self,rank, suit, *args, **kwargs):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    # Write out what card it is
    def __str__(self):
        return f"The card is {self.rank} of {self.suit}."
class Deck():
    # Create an instance of a Deck
    def __init__(self):
    # Firstly create an 'Empty' deck
        self.new_deck = []
        # For every suit, go through the card rank list and append it to the newly created Deck
        # The cards are in order (two of hearts, three of cards ... king of clubs)
        for suit in suits:
            for rank in ranks:
                new_card = Card(rank, suit)
                self.new_deck.append(new_card)

    def shuffle_deck(self):
    # Shuffle the newly created deck
        random.shuffle(self.new_deck)
        return self.new_deck

    def pull_card(self):
        # Pull a card from the top
        return self.new_deck.pop(0)

class Player():
    # Create an instance of a Player, with name and bankroll
    def __init__(self, name, bankroll, *args):
        self.name = name
        self.bankroll = bankroll
        # sum of all the cards player has
        self.sum = 0
        # Player first 'Empty' hand
        self.player_cards = []


    def hit_or_stay(self, new_card):
        # Get the user input, whether HIT or STAY
        user_input = (input("HIT or STAY?\n")).lower()

        if user_input == "hit":
            #print(f"{self.name} just shouted: HIT ME!")
            # Append the new card to the player hand so to say
            card_value = new_card.value
            self.player_cards.append(card_value)
            for i in self.player_cards:
                print(i)


            # print(f"The cards {self.name} has are: {self.player_cards[0]}")


        elif user_input == 'stay':
            print(f"{self.name} just shouted: STAY!")

        else:
            # Make sure user chooses one or another
            Player.hit(self)

    def check_for_sum(self):
            for card in self.player_cards:
                self.sum += card
                print(f"Sum of the cards {self.name} has is: {self.sum}")
                print(self.player_cards)
                # print(self.player_cards)
            return self.sum


    def __str__(self):
    # Check how many cards player has - Just for check purposes
        if len(self.player_cards) == 1:
            pass
            # return f"Player {self.name} has {len(self.player_cards)} card."
        else:
            pass
            # return f"Player {self.name} has {len(self.player_cards)} cards."


class Dealer():

    def __init__(self):
        pass




game_on = True
partija = True

while game_on:
    new_deck = Deck()
    new_deck.shuffle_deck()

    while partija:

        new_player = Player("John", "500")
        new_player.hit_or_stay(new_deck.pull_card())

        if new_player.check_for_sum() > 21:
            print("Dealer wins!")
            partija = False
        else:
            continue
