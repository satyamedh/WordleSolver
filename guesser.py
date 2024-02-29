import os
from termcolor import colored, cprint
import random
import re

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

done = False
while not done:
    # ask for the green words
    green_words = input("Enter the green words(Example: if l and r are green in learn, l__r_): ")

    if "_" not in green_words:
        print("Congrats on cheating ;)")
        done = True
        continue

    # ask for the yellow words
    yellow_words = input("Enter the yellow words(no order. Example: if a and n are yellow in learn: an): ")
    # ask for the gray words
    gray_words = input("Enter the gray words(no order. same as yellow): ")


    # regex building. just replace the _ with .
    green_re = f'^{green_words.replace("_", ".")}'

    # for yellow, just use the | operator
    yellow_re = f'{"|".join(yellow_words)}'

    # for gray, same thing
    gray_re = f'{"|".join(gray_words)}'

    # filter the words
    for word in words:
        green_result = (re.findall(green_re, word) if green_words else True)
        yellow_result = (re.findall(yellow_re, word) if yellow_words else True)
        gray_result = (re.findall(gray_re, word) if gray_words else False)
        if green_result and yellow_result and not gray_result:
            print(word)
