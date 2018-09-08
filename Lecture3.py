#num = float(input('enter a number'))

#if num > 0:
    #print('then it is a positive number')
#elif num < 0:
    #print('this is a negative number')
#else:
   #print('this must be zero')

age = int(input('please enter your age: '))
gender = input('Gender? Please enter M or F: ')
status = input('please enter your status S or M: ')

if age >= 25 and gender == 'F' and status == 'M':
    print("Congrats! You are eligible for %25 discount")
elif age >= 30 and gender == 'M' and status == 'M':
    print("Congrats! You are eligible for %25 discount")
elif age >= 40 or (gender =='F' and age >20):
    print("Congrats! You are eligible for %10 discount")
else:
    print("sorry, no discount!")




