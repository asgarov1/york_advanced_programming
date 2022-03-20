import json
import xml.etree.ElementTree as ET


def create_xml_elements():
    student_xml = ET.SubElement(xml_root, 'student')
    ET.SubElement(student_xml, 'id').text = str(student['id'])

    students_full_name = student['fullName']
    full_name_xml = ET.SubElement(student_xml, 'fullName', title=students_full_name['title'])
    ET.SubElement(full_name_xml, 'firstName').text = students_full_name['first']
    ET.SubElement(full_name_xml, 'surname').text = students_full_name['surname']
    other_xml = ET.SubElement(full_name_xml, 'other', num=str(len(students_full_name['other'])))

    for name in students_full_name['other']:
        ET.SubElement(other_xml, 'name').text = name

    ET.SubElement(student_xml, 'age').text = str(student['age'])
    ET.SubElement(student_xml, 'city').text = student['city']


with open('People.json', 'r') as input_file:
    data_as_json = json.load(input_file)
    xml_root = ET.Element('students')

    for student in data_as_json['students']:
        create_xml_elements()

    xml_tree = ET.ElementTree(xml_root)
    xml_tree.write('json_to_xml.xml')
