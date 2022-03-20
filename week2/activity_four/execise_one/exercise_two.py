from week2.activity_four.execise_one.exercise_one import find_word_in_file, count_by_regex_in_file, \
    replace_symbols_from_file, find_all_by_regex_in_file

assert 391 == find_word_in_file('The_Raven.txt', 'shrieked')
assert 'Not found' == find_word_in_file('The_Raven.txt', 'bleak')
assert 5 == count_by_regex_in_file('The_Raven.txt', '\\b\\w*pp\\w*\\b')
assert '!' not in replace_symbols_from_file('The_Raven.txt', '!', '#')

expected = ['tapping', 'Tis', 'tapping', 'this', 'that', 'tempest', 'token', 'that', 'thy', 'thy', 'thy']
assert expected == find_all_by_regex_in_file('The_Raven.txt', '\\b[tT]{1}\\w*[^e\\s\\t,.]\\b')
