x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
elif x == 99:
    print('I guessed your number')
elif x == 56:
    print('I guessed your number')
elif x == 78:
    print('I guessed your number')


else:
    print('I give up')
