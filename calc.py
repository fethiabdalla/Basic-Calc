# Define our function
def calculate():    
    operation = input(''' 
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
% for modulo
** for power
// for floor division
''')

    num_1 = float(input('Enter your first number: '))
    num_2 = float(input('Enter your second number: '))

    if operation == '+':
        print(f'{num_1} + {num_2} = ')
        print(num_1 + num_2)

    elif operation == '-':
        print(f'{num_1} - {num_2} = ')
        print(num_1 - num_2)

    elif operation == '*':
        print(f'{num_1} * {num_2} = ')
        print(num_1 * num_2)

    elif operation == '/':
        print(f'{num_1} / {num_2} = ')
        print(num_1 / num_2)

    elif operation == '%':
        print(f'{num_1} % {num_2} = ')
        print(num_1 % num_2)

    elif operation == '**':
        print(f'{num_1}**{num_2} = ')
        print(num_1**num_2)
    
    elif operation == '//':
        print(f'{num_1}//{num_2} = ')
        print(num_1//num_2)
    
    else:
        print ('What you have typed is not acceptable, please try again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO
''')
    
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Alright See You Next Time.')
    else:
        again()

calculate()
