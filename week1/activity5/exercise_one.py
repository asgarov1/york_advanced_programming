VOWELS = ['A', 'E', 'I', 'O', 'U']
OTHER = 'Other (non-space) Characters'


def create_vowel_dictionary(input):
    dictionary = {}
    for letter in filter(lambda c: c != ' ', list(input)):
        if letter.upper() in VOWELS:
            dictionary[letter.upper()] = dictionary.get(letter.upper(), 0) + 1
        else:
            dictionary[OTHER] = dictionary.get(OTHER, 0) + 1

    return dictionary


def print_histogram(dictionary):
    for letter in VOWELS:
        print(f'{letter}: {"*" * dictionary.get(letter, 0)}')
    print(f'{OTHER}: {dictionary.get(OTHER)}')


sentence = input('Please enter a sentence')
print_histogram(create_vowel_dictionary(sentence))
