# BlackJack PyGame
# Author >>> Yago Goltara

from os import system       # Imports system() function
from time import sleep      # Imports sleep() function
from art import logo        # Imports logo string from art.py 
import random               # Imports random module

# Function to calculates the score of the players
def scores(cards_list):
    score = 0
    for cards in cards_list:
        score += cards
    return score

# Function to decide who's the winner by comparing players' scores 
def is_user_winner(user_score, pc_score):
    if user_score > pc_score and user_score < 22:
        return True
    elif pc_score > user_score and pc_score < 22:
        return False

# Function to clear the screen 
def clear_screen():
    sleep(0.1)
    system('cls')

# Declares the deck which is gonna be used in the game
card = [2,3,4,5,6,7,8,9,10,10,10,10,11]

# Flag to a further while loop 
wanna_play_again = True

# Greetings
print(logo)
print("Welcome to the Blackjack Game!")
name = input("First of all, tell me your name: ")
print(f"\nOk, {name}. I'll be the dealer.\nCall me Mr. PyDealerbot. Pretty unique, right?")

ans = input("Now, type 'y' to start the game:\n").lower()

# Condition to start the Blackjack game
if not ans == 'y':
    print(f"ERROR. Please, {name}, restart the game.") 

elif ans == 'y':
    while wanna_play_again == True:
        clear_screen()     # Initializes the game

        user_cards = []    # Creates the user hand
        pc_cards = []      # Creates the pc hand

        # Initial cards
        for i in range(2):
            user_cards.append(random.choice(card))
            pc_cards.append(random.choice(card))

        # Initial scores
        pc_score = scores(pc_cards)
        user_score = scores(user_cards)

        # Prints user cards and the first pc card
        print(logo)
        print(f"Your initial cards are: {user_cards}    |   Current score: {user_score}")
        print(f"My first card: {pc_cards[0]}")
        
        # Conditions if the user or the pc takes 21 as initial score 
        if user_score == 21 and pc_score == 21: 
            print("DRAW!")
        elif user_score == 21 and pc_score != 0:
            print(f"What??? Blackjack!!! Congratulations, {name}. You win!")
        elif user_score != 0 and pc_score == 21:
            print(f"My initial cards are: {pc_cards}")
            print("MY TIME HAHA BLACKJACK. I WIN! ")

        # Condition if neither user or pc takes 21 as initial score 
        else:
            another_round = True            # Flag to << another_round >> while loop

            while another_round == True:    # While loop which asks the user if it wants to pick one more card
                ans = input("Do you want to pick up another card? Type 'y' or 'n': ").lower()
                if ans == "n":
                    while pc_score < 21 and pc_score < user_score:          # When the user doesn't want to pick up no more cards
                        if 11 in pc_cards:                                  # The PC is gonna take some cards until two conditions:
                            if pc_score > 21:                               # 1 - Its own score be higher than 21
                                pc_cards[pc_cards.index(11)] = 1            # 2 - Or its own score be higher than user's score
                        pc_cards.append(random.choice(card))
                        pc_score = scores(pc_cards)
                    
                    # Displays the PC's cards and score
                    print(f"My cards: {pc_cards}    |   My score: {pc_score}")

                    # Compare the User and PC scores and pick the winner
                    if pc_score == user_score:
                        print("DRAW!")
                    elif pc_score > 21:
                            print(f"Oh my god. I took {pc_score} points... You win!")
                    else:
                        if is_user_winner(user_score, pc_score) == True:
                            print(f"Congratulations, {name}! You win!!!")
                        else:
                            print(f"Oh oh... I win! You should practice more {name}.")
                    another_round = False

                elif ans == "y":                                            # When the user wants to pick up one more card
                    user_cards.append(random.choice(card))
                    user_score = scores(user_cards)
                    if 11 in user_cards:
                        if user_score > 21:                                 # If there are an 11 in the user's deck and its' score is above 21
                            user_cards[user_cards.index(11)] = 1            # The "11" will be replaced to "1"
                            user_score = scores(user_cards)

                    # Displays the user's cards                                       
                    print(f"Your current cards: {user_cards}    |   Current score: {user_score}")
                    
                    # If during this "pick up cards" the score goes above 21, the user automatically loses 
                    if user_score > 21:
                        print(f"My current cards:{pc_cards}     |   My score: {pc_score}")
                        print("You lose!")
                        another_round = False
                
                else:
                    print(f"Plase, {name}. Insert a valid answer...")    
                    sleep(0.5)    

        # Asks the user if he/she wants to play another round                                   
        if not input("\nDo you want to play again? Type 'y' or 'n':\n") == 'y':
            wanna_play_again = False
            print(f"See you soon, {name}!")