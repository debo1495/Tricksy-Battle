import random
import time
import matplotlib.pyplot as plt


# Constants
opening = "#################################################\nWELCOME TO MY GAME\n"



# Functions 
def game_countdown():
    print("################################################# GET READY ################################")
    count = 1
    while (count <= 3):
        print(f"################################################# {count} ################################")
        count += 1
        time.sleep(1)
        

def check_score(player1_score, player2_score):
    """
    This function checks each players score and prints end game functions if either player_score = 9 or if the score is 16 to 0. 
    If the score is 16 to 0 the loser automaticlly scores 17 points as they "shoot to the moon" and the game is over.
    """
    game_winner = None
    if player1_score >=9 and player2_score >= 1:
        game_winner = "player1"
        print(f"The game is over!! {game_winner} has taken victory!! Congratulations ")
    elif player2_score >= 9 and player1_score >= 1:
        game_winner = "player2"
        print(f"The game is over!! {game_winner} has taken victory!! Congratulations ")
    elif player1_score == 16 and player2_score == 0:
        player2_score = 17
        game_winner = "player2"
        print(f"{game_winner} has shot to the moon!!! He now has {player2_score} points. Game Over. This is is an automatic victory for {game_winner}  ")
    elif player2_score == 16 and player1_score == 0:
        player1_score = 17
        game_winner = "player1"
        print(f"{game_winner} has shot to the moon!!! He now has {player1_score} points. Game Over. This is an automatic victory for {game_winner} ")
    return game_winner
# player_1_score = 16
# player_2_score = 0
# round = 17
# game_winner = check_score(player_1_score, player_2_score)
    
    


def print_hand(hand):
    for i, card in enumerate(hand):
        print(f"{i}: {print_card(card)}")
    
        
def get_value(card):
    """
    This function takes a card tuple as a parameter and returns its value.
    """
    if "Ace" in card[0]:
        return 1
    elif "2" in card[0]:
        return 2 
    elif "3" in card[0]:
        return 3
    elif "4" in card[0]:
        return 4
    elif "5" in card[0]:
        return 5
    elif "6" in card[0]:
        return 6
    elif "7" in card[0]:
        return 7
    elif "8" in card[0]:
        return 8
    elif "9" in card[0]:
        return 9
    elif "10" in card[0]:
        return 10
    elif "Jack" in card[0]:
        return 11
    elif "Queen" in card[0]:
        return 12

def print_card(card):
    """
    Takes in card tuple and returns a string for the card to be printed
    """
    card_string = str(card[0] +" of "+ card[1])
    return card_string

def get_suit(card):
    """
    Takes in card tuple and returns suit
    """
    return str(card[1])

def create_suit_deck(deck, suit):
    """
    Creates A deck with selected suits
    """
    new_deck = []
    for card in deck:
        if card[1] == suit:
            new_deck.append(card)
    return new_deck

def get_choice(hand, player):
    while True:
            try:
                choice = int(input(f"{player} please select a card from your hand above Play a card. Input index starting from 0: "))
                if choice >= 0 and choice < len(hand):
                    return choice
                print("invalid index")
            except ValueError:
                print("Invalid input. Please type in a number")
def renew_hand(deck, player1_hand, player2_hand):
    """
    When each player is down to four cards,  four more cards are distributed to them and taken from the deck
    """
    for _ in range(4):
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())
    return deck, player1_hand, player2_hand

def play_round(player1_hand, player2_hand, lead):
#TODO Make a function that plays a card. It takes a random card from the hand and puts in the players hand then deletes the card from the deckdef play_round(player1_hand,player2_hand):
    if lead == "player1":
        lead_hand =player1_hand
        response_player_hand = player2_hand
        response_player = "player2"
    elif lead == "player2":
        lead_hand = player2_hand
        response_player_hand = player1_hand
        response_player = "player1"
    # Lead player chooses a card:
    print(f"{lead} is leading this round")
    query = input(f"{response_player} look away. {lead} Press enter on your keyboard to see your deck. ")
    print_hand(lead_hand)
    choice = get_choice(lead_hand, lead)       
    lead_card = lead_hand.pop(choice)
    lead_suit = get_suit(lead_card)
    lead_card_value = get_value(lead_card)
    print(f"{lead} plays {print_card(lead_card)} with a value of {lead_card_value}")

    
 
    #TODO Get value of lead card 
    temp_hand = create_suit_deck(response_player_hand, lead_suit)
    if not temp_hand:
        query = input(f"{response_player} look away. {lead} press anything on your keyboard + enter to see your deck ")
        print("You have no matching suites. Pick a card from your whole deck to discard")
        print_hand(response_player_hand)
        choice = get_choice(response_player_hand, response_player)
        response_card = response_player_hand.pop(choice)
        print(f"{response_player} discards {print_card(response_card)}")
        winner = lead 
        return winner, player1_hand, player2_hand
    else:
        query = input(f"{lead} look away. {response_player} press anything on your keyboard + enter to see your deck: ")
        print(f"{response_player} you must follow with {lead_suit} \n Choose a Card:")
        print_hand(temp_hand)
        choice = get_choice(temp_hand, response_player)
        response_card = temp_hand[choice]
        response_player_hand.remove(response_card)
        response_card_value = get_value(response_card)
        print(f"{response_player} plays {response_card} with a value {response_card_value}")        
    if lead_card_value > response_card_value:
        winner = lead
    elif lead_card_value < response_card_value:
        winner = response_player
    else:
        winner = None
    
    return winner, player1_hand, player2_hand
def plot_final_scores(player_1_score, player_2_score):
    players = ["player1","player2"]
    scores = [player1_score, player2_score]
    colors = ["red", "blue"]
    plt.bar(players, scores, color = colors)
    plt.title("Final Scores")
    plt.ylim(0, 17)
    plt.show()
    plt.figure(figsize=(6,4))
    plt.grid(axis = "y", linestyle = "-", alpha = 0.7)
# plot_final_scores(9, 4)
# card = ("Queen", "Spades")
# card[0]
# get_value(card=card)
# print_card(card= card)
# suit = get_suit(card)
# print(suit)

#TODO Make a Deck of 48 Cards Using A dictionary using a list wit tuples

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9","10", "Jack", "Queen"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
deck = []
for card in cards:
    for suit in suits:
        deck.append((card,suit))
# print(deck)
#TODO Make a list with thier current hand
random.shuffle(deck)
# print(deck)
player1_hand = []
player2_hand = []
i = 0
#TODO Give each player eight cards
for i in range(8):
    player1_hand.append(deck.pop())
    player2_hand.append(deck.pop())
player1_hand

#TODO use random to decide which player will pick first
round = 1
player1_score = 0
player2_score = 0
lead = random.choice(["player1", "player2"])
time.sleep(1)
print(opening)
game_countdown()
print(f"{lead} has been selected to go first")
while round <= 16:
    game_winner = check_score(player1_score, player2_score)
    if game_winner:
        break

    print(f"Round: {round}")
    time.sleep(1)
    winner, player1_hand, player2_hand = play_round(player1_hand, player2_hand, lead)
    if winner == "player1":
        print(f"{winner} has won round: {round}")
        player1_score += 1
    elif winner == "player2":
        print(f"{winner} has won round: {round}")
        player2_score+=1
    else:
        print(f"Round {round} ended in a tie. ")
    print(f"Scores: Player 1: {player1_score}, Player 2: {player2_score} \n ################################")
    if deck:
        revealed_card = deck.pop()
        print(f"Revealed card from deck: {print_card(revealed_card)}")
    if winner:
       lead = winner

    if len(player1_hand) == 4 and len(player2_hand) == 4 and len(deck) >= 8:
        deck, player1_hand, player2_hand = renew_hand(deck, player1_hand, player2_hand)
    round += 1
    time.sleep(1)
if not game_winner:
    print(f"Final Scores:\n Player 1: {player1_score}\n Player 2:{player2_score}\n ##################################")
    if player1_score > player2_score:
            game_winner = "player1"
            print("Player 1 won the game")
    elif player1_score < player2_score:
        game_winner = "player2"
        print("Player 2 won the Game")
    else:
        print("The game ended in a tie")
    plot_final_scores(player1_score,player2_score)



#Suggestions:
 
 #   Define classes for core components:

#Card: Representing individual cards with attributes like rank and suit.

# deck : Managing the collection of cards, including shuffling and drawing.

# Player: Handling player-specific data such as hand and score.

# Game: Orchestrating the overall game flow.


# Use snake_case for function and variable names (e.g., get_choice instead of getChoice).

# Ensure consistency in naming across the codebase.














