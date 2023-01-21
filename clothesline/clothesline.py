import random


def main():
    secret_word = pick_secret_word()
    secret_word_length = len(secret_word)
    guess = "-" * secret_word_length
    incorrect_count = 0
    letters_guessed = []

    while incorrect_count < 8 and guess != secret_word:
        print_clothesline(incorrect_count)
        print()
        print("Word:    " + guess)
        print("Guesses: " + " ".join(letters_guessed))
        print()
        letter = input("""Guess a letter...if you dare!
> """)[0]
        letters_guessed.append(letter)
        is_correct = is_letter_in_word(letter, secret_word)
        clear_screen()
        if is_correct == True:
            guess = update_guess(guess, letter, secret_word)
        else:
            incorrect_count = incorrect_count + 1

    if incorrect_count == 8:
        print_clothesline(incorrect_count)
        print()
        print("Word:    " + guess)
        print("Guesses: " + " ".join(letters_guessed))
        print()
        print("The word was '" + secret_word + "' -- you LOSE! Good DAY sir!")
    else:
        print_clothesline(incorrect_count)
        print()
        print("Word:    " + guess)
        print("Guesses: " + " ".join(letters_guessed))
        print()
        print("You win!")

# old pick_secret_word function using a list manually populated by me

# def pick_secret_word():
#     secret_word_options = ["mother", "yeet", "brand", "leave", "director", "disagreement", "muscle", "harmful", "perceive", "necklace", "draft", "hay",
#                            "expect", "patent", "class", "convert", "cause", "patient", "looting", "mechanical", "neck", "scratch", "spray", "field", "likely", "company"]
#     random_secret_word = random.choice(secret_word_options)
#     return random_secret_word


def pick_secret_word():
    secret_word_options = []
    f = open("easy_words.txt", "r")
    lines = f.readlines()
    for line in lines:
        secret_word_options.append(line.strip())
    random_secret_word = random.choice(secret_word_options)
    return random_secret_word


# Alternative code for pick_secret_word function:
# def pick_word():
#     word_filename = "easy_words.txt"
#     word_file = open(word_filename)
#     all_text = word_file.read()
#     all_words = all_text.splitlines()
#     word_file.close()

#     word = random.choice(all_words)
#     return word


def clear_screen():
    print("\033[H\033[J", end="")


def is_letter_in_word(letter, word):
    if letter in word:
        return True


def print_clothesline(incorrect_count):
    if incorrect_count == 0:
        print(image1)
    elif incorrect_count == 1:
        print(image2)
    elif incorrect_count == 2:
        print(image3)
    elif incorrect_count == 3:
        print(image4)
    elif incorrect_count == 4:
        print(image5)
    elif incorrect_count == 5:
        print(image6)
    elif incorrect_count == 6:
        print(image7)
    elif incorrect_count == 7:
        print(image8)
    elif incorrect_count == 8:
        print(image9)
    print("Number of incorrect guesses left: " + str(8 - incorrect_count))


def update_guess(old_guess, letter, secret_word):  # this one is a doozy!
    new_guess = ""
    for index in range(len(old_guess)):
        if secret_word[index] == letter:
            new_guess = new_guess + letter
        else:
            new_guess = new_guess + old_guess[index]

    return new_guess


# this is Matt's breakdown of what is happening in the above update_guess function.

# guess = "_____"
# word = "apple"  # [a,p,p,l,e]
# letter1 = "a"
# letter2 = "l"
# letter3 = "e"
# letter4 = "z"


# def update_guess(old_guess, letter,  word):
#     input("old guess: " + old_guess)
#     input("letter: " + letter)
#     new_guess = ""                 # [a,p,p,l,e]
#     for index in range(len(word)):  # [0,1,2,3,4]
#         input("word index: " + word[index])
#         if word[index] == letter:
#             new_guess = new_guess + letter
#             input("new guess: " + new_guess)
#         else:
#             new_guess = new_guess + old_guess[index]
#             input("new guess: " + new_guess)

#     print()
#     return new_guess


# guess = update_guess(guess, letter1, word)
# guess = update_guess(guess, letter2, word)
# guess = update_guess(guess, letter3, word)
# guess = update_guess(guess, letter4, word)


# All 9 ASCII images

image1 = r"""
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````


"""

image2 = r"""
=====!=====!=======!=====!=======!=====!=======!===========
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|


"""

image3 = r"""
=====!=====!=======!=====!=======!=====!===================
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
                                            _.~.,_.._
                                             ```````

"""

image4 = r"""
=====!=====!=======!=====!=======!=========================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
                                            _.~.,_.._
                                             ```````
"""

image5 = r"""
=====!=====!=======!=====!=================================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""

image6 = r"""
=====!=====!=======!=======================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""

image7 = r"""
=====!=====!===============================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""

image8 = r"""
=====!=====================================================
    /'\
   /   .\
   '|  ='
    |   |
    |   |
    `-._|
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""

image9 = r"""
===========================================================






  _.~.,_.._     _.~.,_.._     _.~.,_.._     _.~.,_.._
   ```````       ```````       ```````       ```````
"""

# runs the program

clear_screen()

main()
