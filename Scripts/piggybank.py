# estimated yearly interest 

print('how many years will you be saving?')
years = int(input('Enter years: '))

print('Your current account amount? ')
principal = float(input('Enter current account balance: '))

print('Amount you plan to invest monthly?')
monthly_invest = float(input('Enter amount: '))

print('What is a est of the yearly interest of this investment?')
interest = float(input('Enter interest in decimal numbers (10% = 0.1): '))

print(' ')

monthly_invest = monthly_invest * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + monthly_invest) * (1 + interest)

print('The total amount that will be in your account after {} years: '.format(years) + str(final_amount))