FIRST_LINE = ' M   T   W  Th   F   S  Su'


def getCalendar(days, startDay):
    result = FIRST_LINE + '\n'

    initial_spaces = ' ' * ((startDay - 1) * 4)
    line = initial_spaces
    for i in range(1, days + 1):
        if len(line) >= len(FIRST_LINE):
            result += line + '\n'
            line = ''
        line += str(i).rjust(2, ' ') + '  '

    result += line
    return result


print('Please input number of days in the calendar:');
days = int(input())

print('Day of the week to start with:\n')
startDay = int(input())

print(getCalendar(days, startDay))
