import json
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['university']
collection = db['students']

with open('People.json', 'r') as input_file:
    students = json.load(input_file)['students']

# collection.insert_many(students)

print('The full name of anyone over 25:')
for result in collection.find({'age': {'$gt': 25}}, {'fullName.first': 1, 'fullName.surname': 1, '_id':0}):
    print(result)
print()

print('The id of anyone who does not have any middle names:')
for result in collection.find({'fullName.other.0': None }, {'_id':1}):
    print(result)
print()

print('Count how many men and how many women (separately) are not living in Tokyo:')
found = list(collection.find({'city': {'$ne': 'Tokyo'}}))
number_of_men_not_in_tokio = sum(student['fullName']['title'] == 'Mr' for student in found)
print(f"Men:  {number_of_men_not_in_tokio}")
print(f"Women:  {len(found) - number_of_men_not_in_tokio}")

# cleaning up
# collection.drop()
