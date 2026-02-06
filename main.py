from datetime import datetime, timedelta
import random
import re # Використовуйте модуль re для регулярних виразів для видалення непотрібних символів.

# ============================================= Завдання 1
# current_date = Поточна дата
def get_days_from_today(date, current_date = datetime.today()):
    try:
        # дата отримана на вході
        in_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f'Inccorrect date value => {date}')

    # Розрахунок кількості днів
    return current_date.toordinal() - in_date.toordinal()


print (f'{'='*8} task #1 checking' )
days = get_days_from_today('2021-10-09')
print (f'days: {days}')

days = get_days_from_today('2021-10-09',  current_date = datetime(year=2021,month=5 ,day=5))
print (f'days: {days}')

try:
    # to check incorrect datetime value in string
    days = get_days_from_today('202109-45',  current_date = datetime(year=2021,month=5 ,day=5))
    print (f'days: {days}')
except Exception as e:
    print(e)


# ============================================= Завдання 2
def get_numbers_ticket(min, max, quantity):
    # Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
    if min < 1: raise ValueError('min is less than 1')
    if max > 1000: raise ValueError('min is bigger than 1000')
    if min > max: raise ValueError('min is bigger than max')
    if (max-min) < quantity: raise ValueError('insufficient quantity for unique numbers')

    tickets = set()
    while len(tickets) < quantity :
        tickets.add( random.randrange(min, max) ) # Унікальність результату: усі числа у видачі повинні бути унікальними.

    return sorted(tickets) # Відповідність вимогам: результат має бути у вигляді відсортованого списку.

print (f'{'='*8} task #2 checking' )
print (  get_numbers_ticket(1,36,6) )
print (  get_numbers_ticket(1,49,6) )
print (  get_numbers_ticket(1,2,1) )

try:
    print (  get_numbers_ticket(-2,999,6) )
except Exception as e:
    print(e)

try:
    print (  get_numbers_ticket(1,9,16) )
except Exception as e:
    print(e)

try:
    print (  get_numbers_ticket(91,19, 6) )
except Exception as e:
    print(e)

try:
    print (  get_numbers_ticket(1,1,1) )
except Exception as e:
    print(e)

# ============================================= Завдання 3
def normalize_phone(phone_number):
    # Видаліть всі символи, крім цифр та '+', з номера телефону.
    pattern = r'\d+'
    ph = ''.join( re.findall(pattern,phone_number) )
    if ph.startswith('38') == False: ph = f'38{ph}'
    if len(ph) != 12 : raise ValueError(f'unable to extract phone number => {phone_number}')
    return f"+{ph}"   # Перевірте, чи номер починається з '+', і виправте префікс згідно з вказівками.


print (f'{'='*8} task #3 checking' )
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
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

try:
    normalize_phone('38095112233')
except Exception as e:
    print(e)

# ============================================= Завдання 4
def get_upcoming_birthdays(users, today = datetime.today().date()):
    ret_dict = list()
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").replace(year=today.year).date()

        # Перевірте, чи вже минув день народження в цьому році. Якщо так, розгляньте дату на наступний рік.
        if birthday < today: 
            birthday = birthday.replace(year = birthday.year + 1)
        
        days_beetwen = birthday.toordinal() - today.toordinal()
        # Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день
        if days_beetwen > 7: continue # одразу до обробки наступного

        wd = birthday.weekday()
        if wd > 4: # Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
            birthday = birthday + timedelta( days= (  7 - wd ) )
        
        # Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
        new_user = {}
        new_user['name'] = user['name']
        new_user['congratulation_date'] = datetime.strftime(birthday,'%Y.%m.%d')

        ret_dict.append(new_user)

    return ret_dict


print (f'{'='*8} task #4 checking' )
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Morgan", "birthday": "1990.08.27"},
    {"name": "Jane Stanley", "birthday": "1990.01.22"}
]

upcoming_birthdays = get_upcoming_birthdays(users, datetime.strptime('2024.01.22','%Y.%m.%d').date() )
print("Список привітань на цьому тижні:", upcoming_birthdays)