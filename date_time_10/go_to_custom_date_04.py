# program to go to a Specific day in a date

from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

print("------Go to the first day in this month--------")  # 1-7-2024
first_date = today + relativedelta(day=1)
print('first Day', first_date)

print("------Go to the last day in this month--------") # 31-7-2024
last_date = today + relativedelta(day=31)
print('last Day', last_date)