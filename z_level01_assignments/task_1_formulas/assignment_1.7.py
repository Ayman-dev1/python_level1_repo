import math

loanAmount = 100000
monthlyInterestRate = 0.01
noYears = 7

monthlypayment_1 = loanAmount * monthlyInterestRate
monthlypayment_2 = math.pow(1 + monthlyInterestRate, noYears*12)
monthlypayment_3 = 1 - (1 / monthlypayment_2)

monthlypayment = round(monthlypayment_1 / monthlypayment_3)

print('Monthly payment = ',monthlypayment)

print('-----------------------------------------------')

totalpayment = round(monthlypayment * noYears * 12)

print('Total payment = ',totalpayment)
