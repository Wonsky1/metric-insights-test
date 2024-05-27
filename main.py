import datetime

YEAR = 2023

start_date = datetime.date(YEAR, 1, 1)
end_date = datetime.date(YEAR, 12, 31)

current_date = start_date
while current_date <= end_date:
    print(current_date)
    current_date += datetime.timedelta(days=1)
