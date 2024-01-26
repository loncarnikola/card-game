import random
'''
A Blackjack game where dealer pulls out 3 cards (can be changed)
The next step will be to try and create matrix of probability so dealer can decide 
whether to hit or stay.
'''
# Ranks of the cards
ranks = [
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
]
# All card suits
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# Dictionary for giving value to the rank
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


class Card:
    # Create an instance of a card
    def __init__(self, rank, suit, *args, **kwargs):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    # Write out what card it is
    def __str__(self):
        return f"The card is {self.rank} of {self.suit}."


class Deck:
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


class Player:
    player_turn = True
    # Create an instance of a Player, with name and bankroll

    def __init__(self, name, bankroll, *args):
        self.name = name
        self.bankroll = int(bankroll)
        # sum of all the cards player has
        self.sum = 0
        # Player first 'Empty' hand
        self.player_cards = []
        self.blind = 0

    def place_a_bet(self):

        try:
            """
            Let user choose the value and place the bet if there is that much money
            on his account (bankroll)
            """
            self.blind = float(input("Please, place a bet.\n"))
            if self.blind > self.bankroll:
                print("You don't have that much money.")
                Player.place_a_bet(self)
            else:
                return self.blind
        # Catch if user tries to type in something other than Int
        except ValueError:
            Player.place_a_bet(self)

    def hit_or_stay(self, new_card):
        # Get the user input, whether HIT or STAY

        user_input = (input("HIT or STAY?\n")).lower()

        if user_input == "hit":
            # print(f"{self.name} just shouted: HIT ME!")
            # Append the new card to the player hand so to say
            card_value = new_card.value
            # Let player choose if he/she wants Ace to have value of 1 or 11
            while card_value == 11:
                try:
                    user_choice = int(input("Do you want value of Ace to be: 1 or 11?\n"))
                    if user_choice == 11:
                        card_value = 11
                        break
                    else:
                        card_value = 1
                except ValueError:
                    continue

            self.player_cards.append(card_value)

            print(self.player_cards)

            # print(f"The card {self.name} has is: {self.player_cards[0]}")

        elif user_input == "stay":
            print(f"\n{self.name} stayed at: {self.sum}")
            """
            If user choose "Stay", player_turn ends.
            """
            Player.player_turn = False
            return Player.player_turn
        else:
            # Make sure user chooses one or another
            Player.hit_or_stay(self, new_card)

    # Made it so ... to do what exactly?

    def check_for_sum(self):
        # If player drops out of game at first iteration
        if not self.player_cards:
            return 0
        else:
            # If player has not said to "Stay", add the last card to player sum
            if Player.player_turn:
                self.sum += self.player_cards[-1]
                print(f"Sum of the cards {self.name} has is: {self.sum}")

                return self.sum
            else:
                # If user choose to "Stay", return sum without adding the last card again
                return self.sum

    def __str__(self):
        # Check how many cards player has - Just for testing purposes
        if len(self.player_cards) == 1:
            pass
            # return f"Player {self.name} has {len(self.player_cards)} card."
        else:
            pass
            # return f"Player {self.name} has {len(self.player_cards)} cards."


class Dealer:
    def __init__(self):
        self.dealer_sum = 0
        self.dealer_cards = []

    def dealer_turn(self, new_card):
        # Give dealer a card, same as player, so I could create one func
        card_value = new_card.value
        # print(card_value)
        self.dealer_cards.append(card_value)
        # print(self.dealer_cards)

    def check_dealer_sum(self):
        dealer_sum = sum(self.dealer_cards)
        return dealer_sum


def game_of_blackjack():

    game_on = True
    new_deck = Deck()
    new_deck.shuffle_deck()
    new_player = Player("John", "500")
    dealer = Dealer()

    while game_on:
        #  Create a new instance of a player with bankroll from originaly created + won or lost money
        new_player = Player(new_player.name, new_player.bankroll)

        player_bet = new_player.place_a_bet()

        # Player goes first

        while Player.player_turn:
            # Pulls out a card
            new_player.hit_or_stay(new_deck.pull_card())
            # First check if user goes over 21, the game is over
            if new_player.check_for_sum() > 21:
                print(f"\nDealer wins! {new_player.name} went over 21!\n")
                new_player.bankroll -= player_bet
                break
            # Dealer turn
            if not Player.player_turn:
                for numer_of_dealer_turn in range(3):
                    dealer.dealer_turn(new_deck.pull_card())
                    # Get the sum and store it for player and dealer
                    dealer_sum = dealer.check_dealer_sum()
                    player_sum = new_player.check_for_sum()

                print(f"\nSum of the cards that Dealer has is: {dealer_sum}")

                sum_won = player_bet * 2

                # Check if someone had won
                if player_sum <= 21 and player_sum > dealer_sum or dealer_sum > 21:
                    print(f"\n{new_player.name} wins {sum_won}$ !\n")
                    new_player.bankroll += sum_won
                elif player_sum <= 21 >= dealer_sum and dealer_sum > player_sum:
                    print("Dealer won!")
                    new_player.bankroll -= player_bet
                elif player_sum <= 21 and player_sum == dealer_sum:
                    print(f"\n{new_player.name} wins {sum_won}$ !\n")
                    new_player.bankroll += sum_won


                print(f"{new_player.name} now has: {new_player.bankroll}$.\n")


        another_game = input("Do you want to play another one? Y/N\n").lower()
        if another_game == "y":
            Player.player_turn = True
            game_on = True
        else:
            print("Twas nice playing with you!")


game_of_blackjack()
