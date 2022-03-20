import csv
import re

from week2.activity_two.data_format_util import reorder_dictionary_keys

COLUMN_NAMES = ['Updated', 'Email', 'ID', 'Title', 'Name', 'Company']
CORRECT_COLUMN_ORDER = ['Updated', 'Title', 'Name', 'ID', 'Email', 'Company']


def add_missing_comma_before_id(input):
    space_before_id_regex = '\s(?=\d+[-]{1}\d+)'
    return re.sub(space_before_id_regex, ',', input)


with open('PeopleTrainingDateUpdate.csv', 'r') as csv_file:
    with open('PeopleTrainingDateUpdate_cleaned.csv', 'w') as cleaned_csv_file:
        for json in csv_file:
            cleaned_csv_file.write(add_missing_comma_before_id(json))


def extract_person(line):
    person = {}
    for index, column_value in enumerate(line):
        person[COLUMN_NAMES[index]] = column_value
    return person


def read_updated_csv():
    global csv_file, json
    with open('PeopleTrainingDateUpdate_cleaned.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        result = []
        for json in csv_reader:
            result.append(extract_person(json))
        return result


with open('../exercise_two/PeopleTrainingDate_output.csv', 'r') as original_file:
    with open('outfile.csv', 'w') as output_file:
        # add original data
        for line in original_file:
            output_file.write(line)

        # add updated lines
        people = read_updated_csv()
        for json in reorder_dictionary_keys(people, CORRECT_COLUMN_ORDER):
            print(",".join(json.values()), file=output_file)
