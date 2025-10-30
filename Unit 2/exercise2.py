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
        print('doing calculation..') #For loop
        # Add all the numbers and return the sum of the numbers.
        # this should give us the AdditUp total.
        # HINT: you're going to be using a for loop
        for x in values:
            base = int(x)
            new = []
            new.append[base]
AddItUpMachine()