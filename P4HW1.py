# CTI-110
# P4HW1 - Expenses
# Kevin McCroary
# 10/8/2019

account_balance = float(input('Enter starting amount in account? '))
expense_total = 0
keepgoing = 'y'
loop_count = 0
while keepgoing == 'y':
    loop_count += 1
    expense = print('\nEnter expense ',loop_count,':')
    cost = float(input('$'))
    expense_total += cost
    keepgoing = input('Do you want to enter another expense? (y/n) ')
print('\nAmount in account before expense subtraction $', format(account_balance,',.2f'))
print('Number of expenses entered: ',loop_count)
account_balance -= expense_total
print('\nAmount in account After expense subtraction $',format(account_balance,',.2f'))

# variables for input of account balance, expense total and loop count
# input expense name and cost in loop that can be repeated and take from balance
# display account balance and loop count after expenses
