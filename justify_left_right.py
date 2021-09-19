# Justify String Alignment

a = "Hello".ljust(10, "*")
# Should Output "Hello**********"
b = "Hello".rjust(10, "-")
# Should Output "----------Hello"
c = "Hello".center(20, "=")
# Should Output "=======Hello========"
print(a, b, c)

# Removing with Strip

d = "     World".lstrip()
e = "Light---".rstrip("-")
f = "amp$amp$Darkamp$amp$amp$".strip("amp$")
print(d, e, f)
