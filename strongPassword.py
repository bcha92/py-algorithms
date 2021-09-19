""" Strong Password Detection
Checks if given passwords meet the following criteria:
-Minimum 8 characters
-At least 1 Uppercase character(A-Z)
-At least 1 Lowercase character(a-z)
-At least 1 number(0-9)
-**Bonus** Optional At least 1 non-Alphanumerical symbol(!@#$)"""

def strongPass(password):
    import re
    if len(password) >= 8 \
       and re.search("^[a-zA-Z0-9]+", password) \
       and re.search("[a-z]+", password) \
       and re.search("[A-Z]+", password) \
       and re.search("\d+", password):
        print("PASSED!", password, "is a strong password!")
        pass
    else:
        print("FAILED!", password, "is not a strong password.")
        pass

# Sample password inputs:
passList = [
    "priceydicey", # Weak Password: Should NOT Pass
    "Vicegrip01", # Strong Password: Should Pass
    "steinholt77", # Medium Password: Should NOT Pass
    "1VertigO", # Strong Password: Should Pass
    "Se7en", # Not 8 digits: Should NOT Pass
    "89056012", # Weak Password: Should NOT Pass
    "21yearsagain", # Medium Password: Should NOT Pass
    "YiPP333", # Not 8 digits: Should NOT Pass
    "B0nu$T35t", # **Bonus** Symbols: Strongest Password: Should Pass
    "e^choC4amb3r" # **Bonus** Symbols: Strongest Password: Should Pass
    ]
for word in passList:
    strongPass(word)
