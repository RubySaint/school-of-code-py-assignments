# Code Like A Girl - Assignment 6: Dictionary of You
# Name: Ruby Saint
# Date: 08/03/2024

# Create new dictionary with key-value pairs 
ruby = {'age':'26','occupation':'Spatial Analyst','height':'158cm','hometown':'Launceston'}

# Iterate through each dict pair (by key) and print key & value in f string
for key in ruby:
    print(f'My {key} is {ruby[key]}')

# Add a new item
ruby['favourite colour'] = 'green'

# Remove item
ruby.pop('hometown')

# Update value of existing key
ruby['favourite colour'] = 'red'

# Add multiple key-value pairs
hobbies = {'instrument':'bass','sport':'roller derby'}
ruby.update(hobbies)

# Print as a list of tuples
print(ruby.items())

# Empty dictionary
ruby.clear()







