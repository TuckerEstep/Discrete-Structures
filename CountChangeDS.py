import random
charge = round(random.uniform(1.00, 45.00), 2)
print('Amount owed:', charge)
payment = random.randint(50, 100)
print('You payed the cashier', payment)
change = payment - charge
print('You are owed:', change)

twenty_dollar = 0
five_dollar = 0
dollar = 0
quarter = 0
dime = 0
nickel = 0
pennies = 0



while change>= 20.00:
    twenty_dollar = twenty_dollar + 1
    change = change - 20.00
    
while change >= 5.00:
    five_dollar = five_dollar + 1
    change = change - 5.00
    
while change >= 1.00:
    dollar = dollar + 1
    #print("Dollars: ", dollar)
    change = change - 1.00

while change >= .25:
    quarter = quarter + 1
    change = change - .25

while change >= .10:
    dime = dime + 1
    change = change - .10

while change >= .05:
    nickel = nickel + 1
    change = change - .01

while change >= .01:
    pennies = pennies + 1
    change = change - .01




print('Pennies', pennies)
print('Nickels', nickel)
print('Dimes', dime)
print('Quarters', quarter)
print('1s', dollar) 
print('5s', five_dollar) 
print('20s', twenty_dollar)