# ask user for distinct numbers
print('you will be prompted to enter four distinct numbers, I will tell you the largest')
firstnum = int(input('Please enter the first number: '))
print('First number has been entered')
secondnum = int(input('Please enter the second number: '))
# so far so good, the code works
print('Second number has been entered')
thirdnum = int(input('Please enter the third number: '))
print('Third number has been entered')
fourthnum = int(input('Please enter the fourth number: '))
print('Fourth number has been entered')

# in this section testing if one is the largest number using 'AND' operator
if (firstnum >= secondnum) and (firstnum >= thirdnum) and (firstnum >= fourthnum):
    largest = firstnum
# in this section testing if secondnum is the largest number using 'AND' operator
elif (secondnum >= firstnum) and (secondnum >= thirdnum) and (secondnum >= fourthnum):
    largest = secondnum
# testing thirdnum is the largest number using 'AND' opertor
elif (thirdnum >= firstnum) and (thirdnum >= secondnum) and (thirdnum >= fourthnum):
    largest = thirdnum
# if all else is false, then fourthnum is largest
else:
    largest = fourthnum

print('the largest number is', largest)


