# Code Like A Girl - Assignment 7: Counting Vowels
# Name: Ruby Saint
# Date: 15/03/2024

from vowelcount import vowel_counter
             
name = input("Enter your name to count the vowels: ")
num_vowels = vowel_counter(name)
print(f"My name is {name}.\nI have {num_vowels} vowels in my name!")