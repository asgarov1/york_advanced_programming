from week2.activity_two.data_format_util import COLUMN_NAMES, reformat_data
from week2.activity_two.exercise_one.exercise_one import people


with open('PeopleTrainingDate_output.csv', 'w') as output_file:
    print(",".join(COLUMN_NAMES), file=output_file)
    for json in reformat_data(people):
        print(",".join(json.values()), file=output_file)


