import random
word_list = ['grapes', 'mango', 'pineapple', 'lychee', 'strawberry']
fruit = random.choice(word_list)
print(fruit)
#input("Enter a single letter")
guess = input("Enter a single letter")
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input')
print(guess)
