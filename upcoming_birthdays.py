from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    upcoming_birthdays = []
    today = datetime.today()

    for user in users:
        name, date_of_birth = [i for i in user.items()][0]
        birthday = datetime(
            year=today.year,
            month=date_of_birth.value.month,
            day=date_of_birth.value.day,
        )

        if birthday.weekday() >= 5:
            birthday += timedelta(days=7 - birthday.weekday())

        if birthday.timetuple().tm_yday - today.timetuple().tm_yday in range(0, 7):
            upcoming_birthdays.append(
                {
                    "name": name,
                    "congratulating_date": datetime.strftime(birthday, "%d.%m.%Y"),
                }
            )

    return upcoming_birthdays


if __name__ == "__main__":
    print(
        *get_upcoming_birthdays(
            [{"name": "Yehor", "congratulating_date": "24.03.2000"}]
        )
    )
