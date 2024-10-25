import typing
from datetime import datetime, timedelta, date


# Define the type for a single person
class Person(typing.TypedDict):
    name: str
    birthday: str


class PersonCongratulation(typing.TypedDict):
    name: str
    congratulation_date: str


# Define the type for a list of such dictionaries
PeopleList = typing.List[Person]
PeopleCongratulationList = typing.List[PersonCongratulation]

forward_days = 7
length_week = 7
length_work_week = 5
date_format = "%Y.%m.%d"

# Moved to upper scope for testing
today = datetime.today().date()


def get_upcoming_birthdays(users_list: PeopleList) -> PeopleCongratulationList:
    upcoming: PeopleCongratulationList = []
    for user in users_list:
        # Moved to upper scope for testing
        # today = datetime.today().date()
        birthday = datetime.strptime(user["birthday"], date_format).date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        diff = (birthday_this_year - today).days
        if diff < forward_days:
            weekday = birthday_this_year.weekday()
            if weekday + 1 > length_work_week:
                days = length_week - weekday
                birthday_this_year = birthday_this_year + timedelta(days=days)
            upcoming.append({
                "name": user.get("name"),
                "congratulation_date": birthday_this_year.strftime(date_format)
            })

    return upcoming


if __name__ == "__main__":
    users = [
        {"name": "Name_01_23", "birthday": "1985.01.23"},
        {"name": "Name_01_27", "birthday": "1990.01.27"},
        {"name": "Name_09_29", "birthday": "1990.09.29"},
        {"name": "Name_09_30", "birthday": "1990.09.30"},
        {"name": "Name_10_01", "birthday": "1990.10.01"},
        {"name": "Name_10_07", "birthday": "1990.10.07"},

        {"name": "Name_12_27", "birthday": "1990.12.27"},
        {"name": "Name_12_28", "birthday": "1990.12.28"},
        {"name": "Name_12_29", "birthday": "1990.12.29"},
        {"name": "Name_12_30", "birthday": "1990.12.30"},
        {"name": "Name_12_31", "birthday": "1990.12.31"},

        {"name": "Name_01_01", "birthday": "1990.01.01"},
        {"name": "Name_01_02", "birthday": "1990.01.02"},
        {"name": "Name_01_03", "birthday": "1990.01.03"},
        {"name": "Name_01_04", "birthday": "1990.01.04"},
        {"name": "Name_01_05", "birthday": "1990.01.05"},
        {"name": "Name_01_06", "birthday": "1990.01.06"},
        {"name": "Name_01_07", "birthday": "1990.01.07"},
    ]

    today = date(year=2024, month=1, day=22)
    print(f"Today {today}")
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("This week's list of greetings:", upcoming_birthdays, "\n")

    today = date(year=2024, month=12, day=28)
    print(f"Today {today}")
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("This week's list of greetings:", upcoming_birthdays, "\n")

    today = datetime.today().date()
    print(f"Today {today}")
    users = []
    for delta in range(-2, 8):
        date = today.replace(year=1990) + timedelta(days=delta)
        name = f"Name_{date.month}_{date.day}"
        birthday = date.strftime(date_format)
        users.append({
            "name": name,
            "birthday": birthday
        })
    print("Users:", users, "\n")
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("This week's list of greetings:", upcoming_birthdays, "\n")
