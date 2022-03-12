FIRST_LINE = ' M   T   W  Th   F   S  Su'


def create_calendar(number_of_days, start_day):
    result = FIRST_LINE + '\n'

    initial_spaces = ' ' * ((start_day - 1) * 4)
    line = initial_spaces
    for i in range(1, number_of_days + 1):
        if len(line) >= len(FIRST_LINE):
            result += line + '\n'
            line = ''
        line += str(i).rjust(2, ' ') + '  '

    result += line
    return result


days = int(input('Please input number of days in the calendar: '))
startDay = int(input('Day of the week to start with: '))
print(create_calendar(days, startDay))
