def first():
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
    try:
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
        print(name_list[1000])
    except IndexError as e:
        print('')


def three():
    try:
        randomList = ['67', 53, '30', 72, '10']
        for i in randomList:
            print(float(i) * 10)
    except ValueError as e:
        print('Invalid input!')


def four():
    try:
        file_name = input("Enter File:")
        print(open(file_name).read())
    except FileNotFoundError as e:
        print('No such file found!')

two()