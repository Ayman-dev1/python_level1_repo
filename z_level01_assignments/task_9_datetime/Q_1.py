from datetime import datetime

# problem 1
# dates_list = [datetime(2023, 12, 31),
#               datetime(2023, 8, 15),
#               datetime(2023, 5, 1)
#               ]
# oldest_date = min(dates_list)
#
# print(oldest_date.date())


# problem 2
dates_list = [datetime(2023, 12, 31),
              datetime(2023, 8, 15),
              datetime(2023, 5, 1)
              ]

given_date = datetime(2023, 8, 15)

if given_date in dates_list:
    index = dates_list.index(given_date)
    print(given_date.date(), 'is found in the list at Index = ', index)
else:
    print(given_date.date(), "is Not In The List")
