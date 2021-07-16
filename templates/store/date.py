
from datetime import datetime, timedelta

current_date = "2021-06-24"
days = 4

def calculate(d,n):
    current_date = datetime.strptime(d,'%Y-%m-%d')

    business_days = n

    while business_days > 0:

        current_date += timedelta(days=1)

        weekday = current_date.weekday()

        if weekday >= 5:
            continue

        business_days -= 1

    return current_date


output = calculate(current_date,days)

print(output)

