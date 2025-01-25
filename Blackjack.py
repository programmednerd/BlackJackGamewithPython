import random
# from art import logo (code)

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards) # -> chooses a random card from the list
    return card 


def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2: #if the sum of the cards equalls 21 and the number of cards equalls 2, it should return "Blackjack!".
        return "Blackjack!"
    if 11 in cards and sum(cards) > 21: #if number 11 from the cards appears and the sum of the cards exceeds 21, it should remove 11 from the cards/list and add 1 to the cards.
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score): #compares the two scores and return the associated response based on the end sum
    if u_score == c_score:
        return "Push"
    elif c_score == 21:
        return "Lose, opponent has Blackjack"
    elif u_score == 21:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"
    
def play_game(): # a function that enables us to play and continue playing
    #print logo
    user_cards = [] #empty list for the user's cards
    computer_cards = [] #empty list for the computer's cards
    computer_score = 0
    user_score = 0
    is_game_over = False #a boolean that indicates that the game should keep going

    for _ in range(2): #for loop to choose a random card from the main list
        user_cards.append(deal_card()) #adds the dealt card by the user to the user cards' list
        computer_cards.append(deal_card()) # adds the dealt card by the computer to the computer cards' list

    while not is_game_over:
        """The first while loop is for the user to continue taking cards"""
        user_score = calculate_score(user_cards) #calculates users' score based on the current cards
        computer_score = calculate_score(computer_cards) #calculates computers' score based on the current cards
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 21 or computer_cards == 21 or user_score > 21:
            is_game_over = True #the game is over if only one of these conditions fulfills 
        else: 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 21 and computer_score < 17:
        """The second while loop is for the computer; so the dealer can play as well"""
        computer_cards.append(deal_card())
        computer_score = calculate_score(deal_card())

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play another game of Blackjack? Type 'yes' or 'no': ") == 'yes':
    print("\n" * 20)
    play_game()