# CTI-110
# P4HW2 - MealTipTax
# Kevin McCroary
# 10/17/2019
#

full_reset = 'y'
while full_reset == 'y':
    keep_going = 'y'
    meal_charge = float(input('\nEnter the charge for the meal: '))
    while keep_going == 'y':
        enter_tip = float(input('Enter the tip percent you would like(16%, 18%, or 20%): '))
        if enter_tip == .16 or enter_tip == .18 or enter_tip == .20:
            keep_going = 'n'
        else:
            print('Error, please enter given tip (Enter tip as 0.18 for 18%)')
    sales_tax = float(.06)
    calc_tip = meal_charge * enter_tip
    calc_tax = meal_charge * sales_tax
    total_cost = meal_charge + calc_tip + calc_tax
    print('\nThe food charge is: $', format(meal_charge,',.2f'))
    print('The tip amount is: $', format(calc_tip,',.2f'))
    print('The tax amount is: $', format(calc_tax,',.2f'))
    print('The total charge is: $', format(total_cost,',.2f'))
    full_reset = input('\nWould you like to run again? (y/n): ')

# Ask user for meal charge and tip percent.
# Loop if tip isn't right and calculate with 6% tax if it is.
# Display values and ask user if they want to enter again.
