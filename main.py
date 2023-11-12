from datetime import date
from datetime import datetime, timedelta

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def get_birthdays_per_week(users):
    # now = datetime(2023, 11, 12)
    now = date.today()
    day_week=now.weekday()    
    # now=now.date()    
    dic_bd = {}       
    if len(users)==0:
       return dic_bd   
    for person in users:
        birthday = person.get('birthday').replace(year=now.year)
        delta_days = (birthday - now).days
        if 0 <= delta_days <= 7 or delta_days<=-358:
            week_day_bd=day_week+delta_days
            if week_day_bd>=5:
                week_day_bd=0
            elif week_day_bd<=-358:
                week_day_bd=+365
                if week_day_bd>=5:
                    week_day_bd=0
            weekday_index =week_day_bd
            weekday_name = WEEKDAYS[weekday_index]
            if weekday_name not in dic_bd:
                dic_bd[weekday_name] = []
            dic_bd[weekday_name].append(person.get('name'))

    if len(dic_bd)==0:
        dic_bd={}      
    users= dic_bd    
    return users
if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Bill", "birthday": datetime(1995, 10, 29).date()},
        {"name": "Andrew", "birthday": datetime(1985, 11, 16).date()},
        {"name": "Jill", "birthday": datetime(1990, 11, 17).date()},
        {"name": "Till", "birthday": datetime(2001, 11, 18).date()},
        {"name": "Jan", "birthday": datetime(1995, 11, 19).date()},
        {"name": "Alice","birthday": datetime(2021, 1, 1).date(),}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")


