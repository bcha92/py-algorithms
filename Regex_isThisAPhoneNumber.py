# Is this a Phone Number?

def isPhoneNumber(text):
    # Returns 'False' if characters do not match 12 digits (###-###-####)
    if len(text) != 12:
        return False
    # Also returns false if decimal numbers annotated with '.' is found
    # Also returns false if "-" is not found in positions 3 and 7
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    # Otherwise: 
    return True

# Sample Inputs
print("Is '415-555-4242' a phone number:", isPhoneNumber("415-555-4242"))
print("Is 'Moshi moshi' a phone number:", isPhoneNumber("Moshi moshi"))

# Finding phone number(s) within string.
print("\n")
message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
print("Done")

# Using Regex Objects to find Phone Numbers (Import Regex 're' module)
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("My number is 415-555-4242.")
print("Phone number found: " + mo.group())

# Another way to find Phone Numbers with Regex
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search("My number is 415-555-3131.")
print("Area code is:", mo.group(1))
print("Local number is:", mo.group(2))
print("Phone number is:", mo.group(0))
print("Number in tuple value:", mo.groups())
areaCode, mainNumber = mo.groups()
print("Area code raw:", areaCode)
print("Main number raw:", mainNumber)

# Modified with proper national convention (North American):
phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search("My number is (415) 555-3131.")
print("Area code is:", mo.group(1))
print("Local number is:", mo.group(2))
print("Phone number is:", mo.group(0))
print("Number in tuple value:", mo.groups())
areaCode, mainNumber = mo.groups()
print("Area code raw:", areaCode)
print("Main number raw:", mainNumber)

# Findall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
#brought message back from previous challenge
mo = phoneNumRegex.findall(message)
print(mo) # Should Output the list ['415-555-1011', '415-555-9999']
mo = phoneNumRegex.search("pinoy")
print(mo)

# Wildcard '.'
atRegex = re.compile(r'..at')
mo = atRegex.findall("The cat in the hat sat on the flat mat.")
print(mo) # Should match cat, hat, sat, flat, and mat.
# To match an actual dot, make sure to use backslash "\."
