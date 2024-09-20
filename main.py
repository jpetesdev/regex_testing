# Regular Expressions

import re


"""
Regular Expressions
Descriptions for a pattern of text to match

"""

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # \d is just any digit number and is a string value.

mo = phoneNumRegex.search("My number is 415-555-4242")

print("Phone number found: " + mo.group())

lettersRegex = re.compile(r'[abc]')

letters = lettersRegex.findall("abc 1234 xyz")
letters2 = lettersRegex.match("abc 1234 xyz")
letters3 = lettersRegex.search("abc 1234 xyz")

print(letters)
print(letters2)
print(letters3.group())

text = "my This is my code line."

findARegx = re.compile(r'my')
print(findARegx.search(text)) #Finds the FIRST match of an expression
print(findARegx.findall(text)) #Find every occurance of provided string and puts them in a list
print(findARegx.match(text))  #Looks for pattern match at the beginning of text.
print(findARegx.split(text)) #At each instance of the provided pattern, it will remove that and return the text/data after/between the next occurance.
print(findARegx.sub('new', text)) #Replaces each instance of the provided pattern and returns a brand new string.

##### New Features #####
def add_two(num):
    return num + 2

#This is a change not in newfeature.

#This is a change not in main