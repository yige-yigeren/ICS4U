print("Please type a word")
word = input()
wordlength = len(word)
temp = 0
if wordlength % 2 == 0:
    while temp < wordlength/2:
        if word[temp] != word[wordlength-temp-1]:
            print("This word is not a palindrome")
            exit(0)
        temp += 1
    print("This word is a palindrome")
else:
    while temp < (wordlength-1)/2:
        if word[temp] != word[wordlength-temp-1]:
            print("This word is not a palindrome")
            exit(0)
        temp += 1
    print("This word is a palindrome")
exit(0)