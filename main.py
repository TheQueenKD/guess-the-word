"""
Computer chooses a word
The computer lets me know the amount of letters in a word that I need to guess
I then guess letters for that word one at a time
As I get letters correct, the computer fills in the blanks with those letters
If I guess wrong, the computer keeps track of the wrong letters and displays them for me
I can guess 6 letters wrong
Once I guess wrongly 6 times, the game is over and the computer prints the correct word
If I guess all the correct letters before reaching 6 strikes, the game is over and I win

layout:
choose random word from list
Your word contains n letters: ______
user input for the first letter guessed

be able to take multiple guesses -> while loop
implement a strike system -> check if length of incorrect_guesses is >= 6 ?
"""


import random


WORDS = [
    'nathan',
    'kaitlyn',
]


correct_guess = set()


incorrect_guess = set()


word = random.choice(WORDS)
word_length = len(word)
print(f'Your word contains {word_length} letters!')

# guess = input('What is your guess?\t')
# if guess in word:
#     correct_guess.add(guess)
#     print('Yes! It is the word!')
# else:
#     incorrect_guess.add(guess)
#     print('Not in word!')


while len(incorrect_guess) < 2:  # TODO check if correct word
    guess = input('What is your guess?\t')
    if guess in word:
        correct_guess.add(guess)
        print(f'Yes! It is the word! | You have guessed: '
              f'Correct Letters: {correct_guess} Incorrect Letters: {incorrect_guess}')
    else:
        incorrect_guess.add(guess)
        print(f'Not in word! | You have guessed: '
              f'Correct Letters: {correct_guess} Incorrect Letters: {incorrect_guess}')

print(f'You guessed: Correct:{correct_guess} Incorrect: {incorrect_guess}')
print(f'The correct word was {word.title()}')
