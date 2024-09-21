birth_day = 10
birth_month = 1
birth_year = 1986

current_day = 21
current_month = 9
current_year = 2022
#defining year quarter of my BD
if birth_month in [1, 2, 3]:
    print('first quarter')
elif birth_month in [4, 5, 6]:
    print('second quarter')
elif birth_month in [7, 8, 9]:
    print('third quarter')
else:
    print('forth quarter')

#leap or not leap year
if (birth_year % 4 == 0 and birth_year % 100 != 0) or birth_year % 400 == 0:
    print('leap year')
else:
    print('not leap yeaer')

#how many days came from my BD
#Finding total amount of days from zero point
total_days_amount = 365.25 * current_year + 30 * current_month + current_day

#Finding till my BD days amount from zero point
till_BD_days_amount = 365.25 * birth_year + 30 * birth_month + birth_day

#Finding number days I've been living
lived_days = total_days_amount - till_BD_days_amount
print(f"I've been living {lived_days} days")