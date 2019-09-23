#last value specified is not included
#below for loop will print each value 1 through 19
#i is taken to be short for index
for i in range(1, 20):
    print('i is now {}'.format(i))
#program takes a numeric value as a string. removes the commas. converts string to integer
#prints integer value
# number = '9,223,372,036,854,775,807'
# cleanedNumber = ''
# #len is short for length
# for i in range(0, len(number)):
#     #[i] allows us to access individual characters, characters start from 0 in a string
#     #using the if statement we remove the commas
#     if number[i] in '0123456789':
#         #appends each new value in
#         cleanedNumber = cleanedNumber + number[i]
# #create a variable newNumber to convert cleanedNumber to an int
# newNumber = int(cleanedNumber)
# print('The number is {}'.format(newNumber))

# number = '9,223,372,036,854,775,807'
# cleanedNumber = ''
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print('the number is {} '.format(newNumber))

# #loops though a list of states and prints a welcome message for each
# for state in ['florida', 'georgia', 'alabama']:
#     print('Welcome to ' + state)

#navigating a range in 'steps'
# #The below example will go from 0 to 100 in steps of 5
# for i in range (0,100,5):
#     print('i is {} '.format(i))

#creating a simple times table all the way up to 12*12
for i in range (1,13):
    for j in range (1,13):
        print('{1} times {0} is {2} '.format(i, j, i*j))
    print('===========')

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
# capitalLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# foundCaps = ''
# for i in range(0,len(quote)):
#     if quote[i] in capitalLetters:
#         foundCaps = foundCaps + quote[i]
# print(foundCaps)
#
# for i in range(0,100,7):
#     print('{}'.format(i))