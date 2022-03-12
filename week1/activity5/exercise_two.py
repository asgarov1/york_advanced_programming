def isAnagram(a, b):
    for letter in list(a):
        if letter not in b:
            return False
    return len(a) == len(b)


word_one = input('First word:')
word_two = input('Second word:')
print("These are anagrams" if isAnagram(word_one, word_two) else "These are not anagrams")
