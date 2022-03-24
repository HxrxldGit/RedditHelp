# CTI-110
# P3HW2 - Pizza Order
# Harold Diaz
# 3/24/2022
#

import math

num_students = int(input('How many students do you want to order pizza for?'))
num_sharing = int(input('Enter number of people per pizza ( 1.5, 2, or 3):'))

while num_sharing != 1.5 or num_sharing != 2 or num_sharing != 3:
    print('Should have entered 1.5, 2 or 3')
    print('Run Program again')
    num_sharing = int(input('Enter number of people per pizza ( 1.5, 2, or 3):'))
else:
    if num_sharing == 1.5:
        print('its 1.5')

num_pizzas = (num_students / num_sharing)


#getting the number rounded
#num_pizzas = math.ceil(num_pizzas)

subtotal = int(num_pizzas * 5)
total = int(subtotal * .06)

print('----Pizza Order-------')
print('Number of Students:',num_students)
print(math.ceil('Pizzas Needed:',num_pizzas))
print('Total:',f'{total:.2f}')
