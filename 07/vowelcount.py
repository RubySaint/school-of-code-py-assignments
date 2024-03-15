# Code Like A Girl - Assignment 7: Counting Vowels
# Name: Ruby Saint
# Date: 15/03/2024

def vowel_counter(word):
    vowels = ["a","e","i","o","u"]
    count = 0
    for l in word:
        if l.lower() in vowels:
            count = int(count) + 1
    return count