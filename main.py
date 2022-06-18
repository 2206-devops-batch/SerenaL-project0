import random

with open('words.txt', 'r') as file:
    all_words = file.read()
    words = list(map(str, all_words.split()))
    random_words = random.choice(words)

print(random_words)

tries = 6
guessed_words = []
game_playing = False

print('Welcome to the Game of Hangman!')
print('You have 6 tries to guess the correct word')

while not game_playing:
    print('Please enter a letter')
    user_input = input('Guess: ')
    if tries == 1:
        break

    if user_input == random_words:
        print('Congrats you guess the ', random_words)
        break
    else:
        print('You guessed the wrong letter.')
        tries = tries - 1
        print('Tries left: ', tries)

    