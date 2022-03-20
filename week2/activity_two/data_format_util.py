from datetime import datetime

COLUMN_NAMES = ['Updated', 'Title', 'Name', 'ID', 'Email', 'Company']


def reformat_data(data):
    reordered_people = reorder_dictionary_keys(data, COLUMN_NAMES)
    sorted_people = sort_data_by_updated(reordered_people)
    return sorted_people


def sort_data_by_updated(reordered_people):
    sorted_people = sorted(reordered_people,
                           key=lambda json_object: datetime.strptime(json_object.get('Updated'), '%d/%m/%Y'))
    return sorted_people


def reorder_dictionary_keys(data, new_column_order):
    reordered_people = []
    for person in data:
        reordered_people.append({key: person[key] for key in new_column_order})
    return reordered_people
