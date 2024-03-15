# Code Like A Girl - Assignment 7: Counting Vowels
# Name: Ruby Saint
# Date: 15/03/2024

import vowelcount
             
name = input("Enter your name to count the vowels: ")
num_vowels = vowelcount.vowel_counter(name)
print(f"My name is {name}.\nI have {num_vowels} vowels in my name!")