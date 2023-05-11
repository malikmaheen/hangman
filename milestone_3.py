#input("Guess a letter")
guess = input("Guess a letter ")
while len(guess) == 1 and guess.isalpha():
    print("Good guess")
    break
else:
    print("Invalid letter. Please enter a single alphabetical character.")
import random
word_list = ['grapes', 'mango', 'pineapple', 'lychee', 'strawberry']
word = random.choice(word_list)
if guess in word:
    print(f'Good guess! {guess} was in the word')
else:
    print('Sorry, {guess} is not in the word. Try again.')
def check_guess(guess):