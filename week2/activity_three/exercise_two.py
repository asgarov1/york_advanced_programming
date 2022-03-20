from os.path import exists

def one():
    num1 = input("Enter a number:")
    num2 = input("Enter another number:")
    assert type(num1) == int and type(num2) == int
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num1 > num2 and num1 % num2 == 0:
            print(num1, " is a multiple of ", num2)
        elif num2 % num1 == 0:
            print(num2, " is a multiple of ", num1)
    except ZeroDivisionError as e:
        print("Illegal Argument: 0")


def two():
    try:
        names = input("List of names:")
        name_list = names.split()
        assert(len(name_list) > 1000)
        print(name_list[1000])
    except IndexError as e:
        print('')


def three():
    try:
        random_list = ['67', 53, '30', 72, '10']
        for element in random_list:
            assert type(element) == int or element.isnumeric()

        for i in random_list:
            print(float(i) * 10)
    except ValueError as e:
        print('Invalid input!')


def four():
    try:
        file_name = input("Enter File:")
        assert exists(file_name)
        print(open(file_name).read())
    except FileNotFoundError as e:
        print('No such file found!')

four()