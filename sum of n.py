stri=input()

words=[word.lower() for word in stri.split()]

words.sort()

for word in words:
    print(word)