import os
from termcolor import colored, cprint
import random

PREFIX = "/mnt/c/Users/Satyamedh/PycharmProjects/WordleAI/"
unsorted_words = open(PREFIX + "words.txt", "r").read().split("\n")
print(len(unsorted_words))

words = sorted(unsorted_words)
# remove duplicates
words = list(set(words))
# remove empty strings
words = [word for word in words if word]
# sort
words = sorted(words)

HAX = False

cprint("Start...\n", "red", "on_black")
our_word: str = random.choice(words)
if HAX: print(our_word)
done = False
history_of_prints = []

counter = 0

while not done:
    word = input()
    # check if the word is valid
    if len(word) != 5:
        print("Invalid word. Please enter a word of length 5.")
        continue
    counter += 1
    curr_line = []
    temp_copy = our_word
    if word != our_word:
        for i_char in range(len(our_word)):
            if word[i_char] == temp_copy[i_char]:
                curr_line.append(colored(word[i_char], "white", "on_green"))
                # Replace the character in the temp copy with a _ to avoid double counting
                temp_copy = temp_copy.replace(word[i_char], "_", 1)
            elif word[i_char] in temp_copy:
                curr_line.append(colored(word[i_char], "white", "on_yellow"))
                # same thing here
                temp_copy = temp_copy.replace(word[i_char], "_", 1)
            else:
                curr_line.append(colored(word[i_char], "white", "on_grey"))
        history_of_prints.append(''.join(curr_line))
    else:
        done = True
        history_of_prints.append(colored(word, "white", "on_green"))
        history_of_prints.append(f"Congrats! it took you {counter} tries")
    # we'll be clearing the screen with newlines and reprinting the history of prints cuz fkin pycharm doesn't support clearing the screen
    print("\n" * 50)

    # reprint
    for line in history_of_prints:
        print(line)





