from datetime import datetime
from myhomewormodule import get_days_from_today, get_numbers_ticket, normalize_phone, get_upcoming_birthdays


def main():
    print(f"{'=' * 8} task #1 checking" )
    days = get_days_from_today('2021-10-09')
    print(f'days: {days}')

    print(f"{'=' * 8} task #2 checking" )
    print(  get_numbers_ticket(1,36,6) )
    print(  get_numbers_ticket(1,49,6) )
    print(  get_numbers_ticket(1,2,1) )

    try:
        print(  get_numbers_ticket(-2,999,6) )
    except Exception as e:
        print(e)

    try:
        print(  get_numbers_ticket(1,9,16) )
    except Exception as e:
        print(e)

    try:
        print(  get_numbers_ticket(91,19, 6) )
    except Exception as e:
        print(e)

    try:
        print(  get_numbers_ticket(1,1,1) )
    except Exception as e:
        print(e)

    print(f"{'=' * 8} task #3 checking" )
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print( "Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers )

    try:
        normalize_phone('38095112233')
    except Exception as e:
        print(e)

    print(f"{'=' * 8} task #4 checking" )
    users = [
        {"name": "John Doe", "birthday": "1985.02.23"},
        {"name": "Jane Smith", "birthday": "1990.02.27"},
        {"name": "Jane Morgan", "birthday": "1990.08.27"},
        {"name": "Larysa Pysmenna", "birthday": "1914.02.11"},
        {"name": "Lev Pysarzhevskyi", "birthday": "1874.02.14"},
        {"name": "Pavlo Biloshytskyi", "birthday": "1937.02.07"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print( "Список привітань на цьому тижні:", upcoming_birthdays )

if __name__ == "__main__":
    main()