import random

with open('words.txt', 'r') as file:
    all_words = file.read()
    words = list(map(str, all_words.split()))
    random_words = random.choice(words)

# print(random_words)

tries = 6
guessed_words = []
game_playing = False

print('Welcome to the Game of Hangman!')
print('You have 6 tries to guess the correct word')

while not game_playing:
    print('Please enter a letter or three letter word')

    # Prompt user to enter a letter or word
    user_input = input('Guess: ')

    # Checks if tries is equal to one
    # If tries is equal to one then print Game Over! You were not able to find the word
    # Value of random_word is printed
    # Program ends
    if tries == 1:
        print('Game Over!')
        print('You were not able to find the word', random_words)
        break
    # If one character of user_input is in randomwords then print the message
    if (user_input in random_words):
        print('You guessed the right letter')
    # Otherwise decrement tries by one and print message
    else:
        tries = tries - 1
        print('You guessed the wrong letter.')
        print('Tries left: ', tries)
    # If the user_input and random_words are the same then print message and break out of loop
    if user_input == random_words:
        print('Congrats, you guessed the correct word:', random_words)
        break

    