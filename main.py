import random
from art import logo

# Function to deal a random card from the deck
def deal_card():
    # Return a radom card from the deck
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

# Function to calculate the score of a hand 
def Calculate_score(cards):
    #Take a list of cards and return the score calculate from  the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(u_score,c_score):
    if u_score == c_score:
        return "Draw🙃"
    elif c_score == 0:
        return "Lose, Opponent has BlackJack😱"
    elif u_score == 0:
        return "Win with a Blackjack😎"
    elif u_score > 21:
        return "You went over. You lose😂"
    elif c_score > 21:
        return "Opponent went. You Win😊"
    elif u_score > c_score :
        return "You win😊"
    else:
        return "You lose😂" 
    

# Initialize empty lists for user and computer cards
def play_game():
    
    print(logo)
    user_cards = []
    computer_cards= []
    computer_score = -1
    user_score = -1
    is_game_over = False


    # Deal two cards to each player at the start of the game
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while  not is_game_over:
        user_score = Calculate_score(user_cards)
        computer_score = Calculate_score(computer_cards)
        print(f'Your cards:{user_cards},Current score {user_score}')
        print(f"Computer's First card: {computer_cards[0]}")

        if user_score == 0 and computer_score == 0 and  user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card,Type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = Calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Balckjack? Type 'y' or 'n' : ") == 'y':
    print('\n' * 40)
    play_game()

