from random import randint
import colorama
from colorama import Fore, Back, Style

import os
colorama.init(autoreset = True)

def play():
    while True:
        user_choice = input("Please choose rock - paper - scissors: ").title()
        if (user_choice != "Rock") and (user_choice != "Paper") and (user_choice != "Scissors"):
            print(f"{Fore.RED}Try again, choose one of three items!")
        else:
            break
    computer_choice = randint(0, 2)
    # binding value for computer
    if computer_choice == 0:
        computer_choice = "Rock"
    elif computer_choice == 1:
        computer_choice = "Paper"
    else:
        computer_choice = "Scissors"

    # players choice:
    os.system("cls")
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")    
    # compare user choice with computer choice
    if computer_choice == user_choice:
        print(f"{Fore.GREEN}Draw!")
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print(f"{Fore.GREEN}User win!")
        else:
            print(f"{Fore.GREEN}Computer win!")
    elif user_choice == "Scissors":
        if computer_choice == "Rock":
            print(f"{Fore.GREEN}Computer win!")
        else:
            print(f"{Fore.GREEN}User win!")
    else:
        if computer_choice == "Rock":
            print(f"{Fore.GREEN}User win")
        else:
            print(f"{Fore.GREEN}Computer win!")

while True:
    menu = input("Enter q or Q to quit the game. Enter p or P to play the game: ").upper()
    if menu == "Q":
        print(f"{Fore.BLUE}Good bye~")
        break
    elif menu == "P":
        print(f"{Fore.BLUE}Playing rock - paper - scissors")
        play()
    else:
        print(f"{Fore.RED}Please try again!")
    