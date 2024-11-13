import random
import time

# generate rps
def choose_random():
    return random.randint(0, 2)

# user_input
def get_user_input():
    valid_input = False
    while not valid_input:
        user_input = input("Rock (0), Paper (1), or Scissors (2). Type (3) to quit: ")
        if user_input == "0" or user_input == "1" or user_input == "2" or user_input == "3":
            valid_input = True
            return int(user_input)
        else:
            print("That's not 0, 1, 2, or 3. Please try again.")

# check_win
def check_win(user_input, computer_input):
    win_options = ["It's a tie, how boring...", "Looks like you got lucky this time, you win...", "You lose! Maybe try practicing for another few decades and try again."]
    diff = user_input - computer_input
    return win_options[diff % 3]
    
# game_loop
game_ongoing = True
options = ["Rock", "Paper", "Scissors"]
while game_ongoing:
    user_input = get_user_input()
    if user_input == 3:
        print("Goodbye, quitter.")
        break
    computer_input = choose_random()
    print(f"you chose: {options[user_input]}. Game On!")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print(f"The Rock Paper Scissors Master chose {options[computer_input]}!")
    print(check_win(user_input, computer_input))

