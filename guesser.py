import os
from termcolor import colored, cprint
import random
import re

PREFIX = "/mnt/c/Users/Satyamedh/PycharmProjects/WordleAI/"
words = open(PREFIX + "words.txt", "r").read().split("\n")
words = list(set(words))

# remove empty strings
words = [word for word in words if word]
random.shuffle(words)



def nuke_duplicates(list_of_words):
    return list(set(list_of_words))

done = False
lifetime_green = "_____"
lifetime_yellow = []
lifetime_gray = []
while not done:
    # ask for the green words
    green_words = input("Enter the green words(Example: if l and r are green in learn, l__r_. empty if none): ")
    # make sure the input is either empty or has 5 characters
    if len(green_words) != 5 and green_words != "":
        print("Invalid word. Please enter a word of length 5.")
        continue

    if "_" not in green_words and green_words != "":
        print("Congrats on cheating ;)")
        done = True
        continue

    # ask for the yellow words
    yellow_words = input("Enter the yellow words(no order. Example: if a and n are yellow in learn: an): ")

    # ask for the gray words
    gray_words = input("Enter the gray words(no order. same as yellow): ")



    # for green, update only if the character is not _
    if green_words != "":
        for i in range(5):
            if green_words[i] != "_":
                lifetime_green = lifetime_green[:i] + green_words[i] + lifetime_green[i + 1:]

    # regex building. just replace the _ with .
    green_re = f'^{lifetime_green.replace("_", ".")}'

    lifetime_yellow = nuke_duplicates(lifetime_yellow + list(yellow_words))
    lifetime_gray = nuke_duplicates(lifetime_gray + list(gray_words))

    # if something is in green/yellow and gray, remove it from gray
    for char in lifetime_yellow + list(lifetime_green):
        if char in lifetime_gray:
            lifetime_gray.remove(char)

    counter = 0
    # filter the words
    res = []
    for word in words:
        if counter == 5:
            break
        green_result = (re.findall(green_re, word) if green_re else True)
        yellow_result = (all([char in word for char in lifetime_yellow]) if lifetime_yellow else True)
        gray_result = (any([char in word for char in lifetime_gray]) if lifetime_gray else False)
        if green_result and yellow_result and not gray_result:
            res.append(word)
            counter += 1
    if counter == 0:
        print("No words found. Please check your input.")
        continue
    elif counter == 1:
        print(f"The word is {res[0]}")
        done = True
        continue
    else:
        print(f'Try {", ".join(res)}')

    print("====================================")
