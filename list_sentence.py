# Comma Code

def inSentence(list):
    sentence = ""
    for i in range(len(list)):
        if list[i] == list[0]:
            sentence += list[i].capitalize() + ", "
        elif list[i] == list[-1]:
            sentence = sentence + "and " + list[i] + "."
            break
        else:
            sentence += list[i] + ", "
    print(sentence)

# Example List
spam = ['apples', 'bananas', 'tofu', 'cats']

# Executes Function
inSentence(spam)
