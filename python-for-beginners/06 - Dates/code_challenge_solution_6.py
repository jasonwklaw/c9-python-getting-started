from datetime import datetime, timedelta

# print today's date
today_date = datetime.now()
print(today_date)
# print yesterday's date
one_day = timedelta(days=1)
yesterday_date = today_date - one_day
print(yesterday_date)
# ask a user to enter a date
# print the date one week from the date entered
user_date = input('Please input a date: (dd/mm/yyyy): ')
user_date = datetime.strptime(user_date, '%d/%m/%Y')
one_week = timedelta(weeks=1)
processed_date = user_date - one_week
print(str(processed_date))