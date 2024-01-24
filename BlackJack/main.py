import random
import os
from art import logo

print(logo)
name = input("What's your name? : ")
bit = int(input("What is your bit? : $"))

os.system('clear')


def computer_card(computer_hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_index = random.randint(0, 12)
    computer_hand.append(cards[cards_index])


def display_hands(your_hand, computer_hand, show_computer_card=False):
    print(logo)
    if (show_computer_card):
        print(f"Baris's hand: {computer_hand}")
    else:
        print(f"Baris's hand: [{computer_hand[1]}, X]")
    print(f"{name}'s hand: {your_hand}")


your_hand = []
computer_hand = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
for _ in range(2):
    cards_index = random.randint(0, 12)
    your_hand.append(cards[cards_index])
    cards_index = random.randint(0, 12)
    computer_hand.append(cards[cards_index])

display_hands(your_hand, computer_hand, show_computer_card=False)
while True:
    print("Do you want a new card?")
    print("Yes => type 'y' \nNo  => type 'n'\n")
    choice = input("Your Choice: ")

    if (choice == 'y'):
        cards_index = random.randint(0, 12)
        your_hand.append(cards[cards_index])
        os.system('clear')
        display_hands(your_hand, computer_hand, show_computer_card=False)
        your_result = sum(your_hand)

        if (your_result > 21 and 11 in your_hand):
            your_hand.remove(11)
            your_hand.append(1)

        elif (your_result > 21):
            os.system('clear')
            while sum(computer_hand) < 17:
                computer_card(computer_hand)
            display_hands(your_hand, computer_hand, show_computer_card=True)
            print("You have lose...")
            break
        elif (your_result == 21):
            display_hands(your_hand, computer_hand, show_computer_card=True)
            print("BlackJack, Congratulations!")
            print(f"You win ${bit * 2}. ")
            break

    elif (choice == 'n'):
        while sum(computer_hand) < 17:
            computer_card(computer_hand)
        os.system('clear')
        display_hands(your_hand, computer_hand, show_computer_card=True)
        computer_result = sum(computer_hand)
        your_result = sum(your_hand)

        if (computer_result > 21):
            print("Baris lost - Baris's hand is over 21!")
            print(f"You win ${bit * 2}. ")
        elif (computer_result > your_result):
            print("You lost - Baris's hand is better!")

        elif (computer_result == your_result):
            print("It's a tie!")
            print(f"You win ${bit}. ")

        elif (your_result > computer_result):
            print("You win congratulations!")
            print(f"You win ${bit * 2}. ")

        break

