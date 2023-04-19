
import random
from os import system, name  #used for clearing the termianl
from time import sleep

hang = ["""
   +----+
   |   \|
        |
        |
        |
        |
==========""", """
  +----+
  |   \|
  O    |
       |
       |
       |
==========""", """
  +----+
  |   \|
  O    |
  |    |
       |
       |
==========""", """
  +----+
  |   \|
  O    |
 /|    |
       |
       |
==========""", """
  +----+
  |   \|
  O    |
 /|\   |
       |
       |
==========""", """
  +----+
  |   \|
  O    |
 /|\   |
 /     |
       |
==========""", """
  +----+
  |   \|
  O    |
 /|\   |
 / \   |
       |
=========="""]

def reminder():
    print("----------------------------------------------------------------------------------------------")
    print("| Notice: Some words may contain a space, a dash(-), a period (.), a comma(,), or a colon(:) |")
    print("----------------------------------------------------------------------------------------------\n")
 
def clear():   
    '''
    used to clear the termial based on the os system 
    '''
    # for windows   
    if name == 'nt':   
        _ = system('cls')   
  
    # for mac and linux
    else:   
        _ = system('clear')   

#game mode types
def fruit_choices():
    with open('fruits.txt', 'r') as fileopen:
        name_list = [line.strip().lower() for line in fileopen]
    return name_list

def people_choices():
    with open('famous_people.txt', 'r') as fileopen:
        name_list = [line.strip().lower() for line in fileopen]
    return name_list

def movie_choices():
    with open('movies.txt', 'r') as fileopen:
        name_list = [line.strip().lower() for line in fileopen]
    return name_list

def countires_choices():
    with open('countires.txt', 'r') as fileopen:
        name_list = [line.strip().lower() for line in fileopen]
    return name_list

# play game (and again)
def play_again():
    print("Would you like to play again? Type Yes or No:")
    q1 = input().lower()

    if q1 == "yes" or q1 == "YES" or q1 == "Yes":
        print("Okay, restarting game...\n")
        sleep(1)
        clear()
        hangman()

    elif q1 == "no" or q1 == "NO" or q1 == "No":
        print("Thank you for playing!\n")
        exit()

    else:
        print("Invalid input. Please try again.\n")
        play_again()


def game_mode():
    g_mode = ["Types of Fruit", "Names of People", "Names of Countires", "Names of Movies"]

    print("Usage:\n")
    for i, mode in enumerate(g_mode):
        print(f"    {i+1}. {mode}")
    print()

    game_input = input("Please select a game mode: ")

    if game_input == "1":
        chosen_word = random.choice(fruit_choices())
        print(f"\nYou have chosen '{g_mode[0]}' for your game mode:\n")
        return chosen_word

    elif game_input == "2":
        chosen_word = random.choice(people_choices())
        print(f"\nYou have chosen '{g_mode[1]}' for your game mode:\n")
        return chosen_word

    elif game_input == "3":
        chosen_word = random.choice(countires_choices())
        print(f"\nYou have chosen '{g_mode[2]}' for your game mode:\n")
        return chosen_word

    elif game_input == "4":
        chosen_word = random.choice(movie_choices())
        print(f"\nYou have chosen '{g_mode[3]}' for your game mode:\n")
        reminder()
        return chosen_word
      
    else:
        print("\nInvalid input. Please try again.\n")
        game_mode()

def hangman():
    '''
    This is a Python script for a game of Hangman. The game is played by guessing letters in a word.
    If the guessed letter is in the word, it is revealed in its correct position(s). If the letter is not 
    in the word, a part of the Hangman figure is drawn. The game ends when the word is guessed or when the 
    Hangman figure is complete.
    '''
    print("H A N G M A N")

    chosen_word = game_mode()

    #chosen_word = str(random.choice(read_choices()))
    answer = []
    
    # creates answer table
    x = len(chosen_word)
    for i in range(x):
        answer.append("_")

    total_lives_left = 0
    lives_left = 7
    while total_lives_left < 7:
        right_guesses = 0
        guess = (input("Guess a letter: ").lower())
        if guess in answer:
            print("You guessed", guess)
            print("You've already guessed this letter, try something else")
            print()

            continue
        else:
            if guess in chosen_word:
                right_guesses += 1 # keep track of the correct words guessed
                # prints letter table
                for i in range(len(chosen_word)):
                    if chosen_word[i] == guess:
                        answer[i] = guess
                print(answer)

            else:

                if guess not in chosen_word:

                    # prints ascii art
                    print(hang[total_lives_left])
                    total_lives_left += 1
                    lives_left -= 1

                print(f"You have {lives_left} lives left.")
                print(answer)

        if "_" not in answer:
            print(f"Well done!! you guessed the word '{chosen_word}'\U0001F600.\n")
            print(play_again())
        else:
            if total_lives_left == 7:

                print(f"Ohh No! It looks like you ran out of lives. The word was {chosen_word}\U0001F641.\n")
                print(play_again())

if __name__ == "__main__":
    print(hangman())