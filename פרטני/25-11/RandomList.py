import random

## create 3  random words from  List of all words

words_list = ['shalom','ofer', 'moshe']

password_lenght = int(input(" Eenter Password length : "))

for num in range((password_lenght)):
    letter = random.choice(words_list[num%3])
    print(letter)

