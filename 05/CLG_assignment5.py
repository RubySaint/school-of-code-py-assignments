# Code Like A Girl - Assignment 5: Palindrome Checker #2
# Name: Ruby Saint
# Date: 26/02/2024

#############################################################
# Version 1: Single input
#############################################################

# Prompt user for input
user_input = str(input("Enter a word, number or phrase to check if it's a palindrome: "))

# Iterate through characters of input and join (with no space) only where alphanumeric - to get rid of spaces and special chars, but keep numbers
input_form = ''.join(i for i in user_input.lower() if i.isalnum())

# Convert to list, reverse and convert back to string
input_list = list(input_form)
input_list.reverse()
reverse_str = ''.join(input_list)

# Test for palindrome
if reverse_str == input_form:
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome :(")



#############################################################
# Version 2: Multiple inputs
#############################################################

# Create empty list to hold input phrases
in_phrases = []

print("Welcome to the PalindromeChecker3000. Enter any words, phrases or numbers that you would like to check for palindrome status! Once you are finished entering inputs, type 'done'")
while True:
    # prompt user for input phrase(s)
    phrase = input("Enter a word, phrase or number to check: ")
    if phrase == 'done':
        break
    else:
        in_phrases.append(phrase)

loop_num = 0
palindrome_count = 0

for value in in_phrases:
    loop_num = loop_num + 1
    print(f"Testing input {loop_num} of {len(in_phrases)}: {value}")
    
    formatted_str = ''.join(char for char in value.lower() if char.isalnum())
    input_list = list(formatted_str)
    input_list.reverse()
    reverse_str = ''.join(input_list)

    if reverse_str == formatted_str:
        palindrome_count = palindrome_count + 1
        print(f"Success! {value} is a palindrome\n") #Added line breaks to make output easier to read in console
    else:
        print(f"{value} is not a palindrome\n")

print(f"{palindrome_count} palindromes found")




