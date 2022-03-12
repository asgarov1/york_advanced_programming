def left_side():
    for i in range(1, 5):
        print('*' * i)

def right_side():
    for i in range(1, 5):
        print(('*' * i).rjust(4, ' '))


def center():
    for i in range(1, 6, 2):
        spaces = (5 - i) // 2
        print((' ' * spaces) + ('*' * i))
    for i in range(3, 0, -2):
        spaces = (5 - i) // 2
        print((' ' * spaces) + ('*' * i))


left_side()
print()
right_side()
print()
center()
