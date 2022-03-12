###Exercise 1
# LIFO & FIFO

def lifoPop(my_list):
    my_list.pop()

def fifoPop(my_list):
    my_list.pop(0)

def program(pop_method):
    my_list = []
    while True:
        print('Pick an option')
        print('1. Push')
        print('2. Pop')
        print('3. View')
        print('4. Exit')

        option = int(input())
        if option == 1:
            print('Enter the number')
            my_list.append(int(input()))
        elif option == 2:
            pop_method(my_list)
        elif option == 3:
            print(my_list)
        elif option == 4:
            return


#program(fifoPop)
program(lifoPop)