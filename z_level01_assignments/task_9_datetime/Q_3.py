from datetime import datetime

# Problem 4
dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 8, 15),
    datetime(2023, 8, 15),
    datetime(2023, 5, 1)
]
given_date = datetime(2023, 8, 15)

occurrences = dates_list.count(given_date)

print(given_date.date(), 'occurs', occurrences, 'times')