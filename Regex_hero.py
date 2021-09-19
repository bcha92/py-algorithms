# Multiple Group matching with the Pipe

import re

# Multiple searches with different 'mo' variables
heroRegex = re.compile(r'Batman|Tina Fey')

mo1 = heroRegex.search("Batman and Tina Fey.")
print(mo1.group()) # Should output "Batman"

mo2 = heroRegex.search("Tina Fey and Batman.")
print(mo2.group()) # Should output "Tina Fey"

# Another example of search with multiple groups
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# This will search for a combination of "Bat", "Batman"
# "Batmobile", "Batcopter", "Batbat", "man", "mobile",
# "copter", and "bat".
mo3 = batRegex.search("Batmobile lost a wheel")
print(mo3.group()) # Should output "Batmobile"
print(mo3.group(1)) # Should output "mobile"

# ? mark is optional matching (0 to 1 results for 'wo': "Batman" or "Batwoman")
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group()) # Should output "Batman"
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group()) # Should output "Batwoman"

# This time (\d\d\d-) is optional.
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = phoneRegex.search("My number is 415-555-5656.")
print(mo3.group()) # Should output "415-555-5656"
mo4 = phoneRegex.search("My number is 555-5656.")
print(mo4.group()) # Should output "555-5656"

# * mark is greedy. Will match (0 to infinite results for 'wo')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group()) # Should output "Batman"
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group()) # Should output "Batwoman"
mo3 = batRegex.search("The Adventures of Batwowowoman")
print(mo3.group()) # Should output "Batwowowoman"
mo4 = batRegex.search("Batwowowowowowoman")
print(mo4.group()) # Should output "Batwowowowowowoman"

# but + mark will match 1 to infinite matches.
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search("The Adventures of Batman")
# mo1 == None # Should be True because "Batman" is not searched in this regex
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group()) # Should output "Batwoman"
mo3 = batRegex.search("The Adventures of Batwowowoman")
print(mo3.group()) # Should output "Batwowowoman"

# Curly brackets only matches the {#} specifically.
# In this case, only 3 matches and nothing else.
# All other matches will fail.
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search("HaHaHa")
print(mo1.group()) # Should output "HaHaHa"
mo2 = haRegex.search("Ha")
# mo2 == None # This will therefore not be a match

# This on the other hand will only match 3, 4, 5 "Ha" repetitions
# "HaHaHa", "HaHaHaHa", or "HaHaHaHaHa". All other matches will fail.
haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search("HaHaHa")
print(mo1.group())
mo2 = haRegex.search("HaHaHaHaHa")
print(mo2.group())
