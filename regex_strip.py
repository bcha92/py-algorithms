# Regex Version of Strip

def rStrip(word, char="\s"):
    import re
    stripRegex = re.sub(f"^{char}+", "", word)
    stripRegex = re.sub(f"{char}+$", "", stripRegex)
    print(stripRegex)

words = ["     hello     ", "     goodbye", "again     "]

for greet in words:
    rStrip(greet)
