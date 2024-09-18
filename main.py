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