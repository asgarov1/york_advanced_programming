import re


def read_csv(csv_file):
    result = []
    first_line = csv_file.readline().strip()
    columns = list(first_line.split(","))
    for line in csv_file.readlines():
        result.append(extract_person(line, columns))

    return result


def extract_person(line, column_names):
    person = {}
    line = line.strip()
    columns_values = re.split(r'(".*")|([^,]+)', line)
    columns_cleaned = list(filter(lambda l: l is not None and len(l) > 1, columns_values))
    if len(columns_cleaned) == len(column_names) - 1:
        #means title is missing
        columns_cleaned.insert(0, '')
    for index, column_value in enumerate(columns_cleaned):
        person[column_names[index]] = column_value
    return person


file = open('PeopleTrainngDate.csv', 'r')
people = read_csv(file)
file.close()

