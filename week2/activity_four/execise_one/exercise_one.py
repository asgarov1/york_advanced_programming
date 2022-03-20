import re


def get_file_content(file_name):
    with open(file_name, 'r', encoding="utf8") as input_file:
        return "".join(input_file.readlines())


def find_word_in_file(file_name, regex):
    content = get_file_content(file_name)
    match = re.search(rf'{regex}', content)
    if match is None:
        return 'Not found'
    found_index = match.span()[0]
    return found_index


def count_by_regex_in_file(file_name, regex):
    return len(find_all_by_regex_in_file(file_name, regex))


def replace_symbols_from_file(file_name, symbol_a, symbol_b):
    content = get_file_content(file_name)
    return re.sub(symbol_a, symbol_b, content)


def find_all_by_regex_in_file(file_name, regex):
    content = get_file_content(file_name)
    return re.findall(rf'{regex}', content)


# print(find_word_in_file('The_Raven.txt', 'shrieked'))
# print(find_word_in_file('The_Raven.txt', 'bleak'))
# print(count_by_regex_in_file('The_Raven.txt', '\\b\\w*pp\\w*\\b'))
# print(replace_symbols_from_file('The_Raven.txt', '!', '#'))
# print(find_all_by_regex_in_file('The_Raven.txt', '\\b[tT]{1}\\w*[^e\\s\\t,.]\\b'))
