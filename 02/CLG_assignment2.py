# Code Like A Girl - Assignment 2: Varibles and Strings
# Name: Ruby Saint
# Date: 01/02/2024

original_text = "Hi there! "

shouting_text = original_text.upper()

annoying_text = 10*shouting_text

print(f"My annoying text is: {annoying_text}")
print(f"It has {len(annoying_text)} characters.")

# Alternative solution 1 (using multiline text)
print(f"My annoying text is:\n{annoying_text}\nIt has {len(annoying_text)} characters.")

# Alternative solution 2 (without f-string)
print("My annoying text is: {}\nIt has {} characters.".format(annoying_text,len(annoying_text)))