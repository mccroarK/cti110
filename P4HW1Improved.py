keep_going = 'y'
money_am = float(input('Enter starting amount in account? '))
subtract = 0
loop_count = 0
while keep_going == 'y':
    loop_count += 1
    print('\nEnter expense ', loop_count, ' :', end='')
    expense = float(input())
    subtract+=expense
    keep_going = input('Do you want to enter another expense? (y/n) ')
print('\nAmount in account before expense subtraction $', format(money_am,',.2f'))
print('Number of expenses entered: ', loop_count)
money_am-=subtract
print('\nAmount in account AFTER expenses subtracted is $', format(money_am,',.2f'))
