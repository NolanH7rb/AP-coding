#Warm Up Activity
def AddItUpMachine():
    print("please enter a number")
    number = input()
    values = []
    calculate = '7'
    while number =='7':
        values.append(number)
        print(values)
        print("please enter a number")
        number = input()

AddItUpMachine()

#################################################

def AddItUpMachine():
    print("please enter a number. Please enter 'q' to calculate")
    number = input()
    values = []
    while number != 'stop': #while whatever we type in IS NOT 0 do this...
        values.append(number)
        print(values)
        print("please enter a number")
        number = input()
    else:
        print('done calculation..')

AddItUpMachine()