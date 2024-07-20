# program to get the difference between 2 dates
from datetime import datetime  # from datetime module import datetime class
from dateutil.relativedelta import relativedelta

today = datetime.now()
custom_date = datetime(year=2021, month=1, day=3)
print('today = ', today)
print('custom date = ', custom_date)

difference_in_days = today - custom_date
print(difference_in_days)
print(difference_in_days.days)

print('-------------')
difference_parts = relativedelta(today, custom_date)
print(difference_parts)
print('differ in years = ', difference_parts.years)
print('differ in months = ', difference_parts.months)
print('differ in days = ', difference_parts.days)
