# Code Like A Girl - Assignment 4: Palindrome Checker
# Name: Ruby Saint
# Date: 26/02/2024

# Prompt user for input and convert to lowercase string
user_word = str(input("Is it a palindrome? Enter a word or number to check: "))
user_word = user_word.lower()

# Convert user-input string to a list
user_list = list(user_word)

# Flip list and convert back to str format
user_list.reverse()
reverse_word = ''.join(user_list)

# Check if word is the same in both directions
if reverse_word == user_word:
    print("True")
else:
    print("False")