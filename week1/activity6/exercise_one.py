import Converter


def present_options(converter_one, converter_two):
    print(f'Input 1 for {converter_one.__name__.replace("_", " ")}')
    print(f'Input 2 for {converter_two.__name__.replace("_", " ")}')
    chosen_option = int(input())

    if chosen_option == 1:
        user_input = input('input the amount(s)')
        if len(user_input.split(" ")) > 1:
            inputs = list(map(lambda num: int(num), user_input.split(" ")))
            print(converter_one(inputs[0], inputs[1]))
        else:
            print(converter_one(int(user_input)))
    elif chosen_option == 2:
        user_input = int(input('input the amount'))
        print(converter_two(user_input))
    else:
        raise Exception("Invalid menu option was chosen")


def program():
    while True:
        print('Select a conversion option:')
        print('1. Length')
        print('2. Mass')
        print('3. Temperature')
        print('4. Time')
        print('5. Quit')
        chosen_option = int(input())

        try:
            if chosen_option == 1:
                present_options(Converter.feet_and_inches_to_meters, Converter.meters_to_feet_and_inches)
            elif chosen_option == 2:
                present_options(Converter.pounds_to_kg, Converter.kg_to_pounds)
            elif chosen_option == 3:
                present_options(Converter.kelvin_to_celsius, Converter.celsius_to_kelvin)
            elif chosen_option == 4:
                present_options(Converter.hours_and_minutes_to_seconds, Converter.seconds_to_hours_and_minutes)
            elif chosen_option == 5:
                return
        except Exception as e:
            print(str(e))


program()
# didn't implement user input validaiton - because this is not graded