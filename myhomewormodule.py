from datetime import datetime, timedelta, date
from typing import List, Dict, Any
import random
import re

# ============================================= Завдання 1
def get_days_from_today(date_str: str) -> int:
    """Обчислити кількість днів від заданої дати до сьогодні.
    
    Args:
        date_str: Дата у форматі 'YYYY-MM-DD'
        
    Returns:
        Кількість днів
        
    Raises:
        ValueError: Якщо формат дати невірний
    """
    try:
        in_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f'Inccorrect date value => {date_str}')

    return datetime.today().toordinal() - in_date.toordinal()


# ============================================= Завдання 2
def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> List[int]:
    """Генерувати унікальні випадкові номери лотереї.
    
    Args:
        min_num: Мінімальне число діапазону,більше за 1
        max_num: Максимальне число діапазону, менше за 1000
        quantity: Кількість унікальних номерів для генерування
        
    Returns:
        Відсортований список унікальних номерів
        
    Raises:
        ValueError: Якщо параметри невалідні
    """
    if min_num < 1:
        raise ValueError('min is less than 1')
    if max_num > 1000:
        raise ValueError('max is bigger than 1000')
    if min_num > max_num:
        raise ValueError('min is bigger than max')
    if (max_num - min_num + 1) < quantity:
        raise ValueError('insufficient quantity for unique numbers')

    tickets: set[int] = set()
    while len(tickets) < quantity:
        tickets.add(random.randint(min_num, max_num))

    return sorted(tickets)


# ============================================= Завдання 3
def normalize_phone(phone_number: str) -> str:
    """Нормалізувати номер телефону та додати префікс +38.
    
    Args:
        phone_number: Телефонний номер з будь-якими символами
        
    Returns:
        Нормалізований номер у форматі +38XXXXXXXXXX
        
    Raises:
        ValueError: Якщо не вдалося виділити 10-значний номер
    """
    pattern = r'\d+'
    ph = ''.join(re.findall(pattern, phone_number))
    if not ph.startswith('38'):
        ph = f'38{ph}'
    if len(ph) != 12:
        raise ValueError(f'unable to extract phone number => {phone_number}')
    return f"+{ph}"


# ============================================= Завдання 4
def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Отримати список користувачів з днями народження на наступному тижні.
    
    Args:
        users: Список словників з ключами 'name' та 'birthday' (формат 'YYYY.MM.DD')
        
    Returns:
        Список словників з ключами 'name' та 'congratulation_date'
    """
    today = datetime.today().date()

    upcoming: List[Dict[str, str]] = []
    for user in users:
        birthday = (datetime.strptime(user["birthday"], "%Y.%m.%d")
                    .replace(year=today.year).date())

        # Якщо день народження вже минув цього року, розглядаємо наступний рік
        if birthday < today:
            birthday = birthday.replace(year=birthday.year + 1)

        days_between = birthday.toordinal() - today.toordinal()
        # Розглядаємо дні народження на наступні 7 днів
        if days_between > 7:
            continue

        # Якщо день народження на вихідний, переносимо на понеділок
        weekday = birthday.weekday()
        if weekday > 4:
            birthday = birthday + timedelta(days=(7 - weekday))

        congratulation = {
            'name': user['name'],
            'congratulation_date': birthday.strftime('%Y.%m.%d')
        }
        upcoming.append(congratulation)

    return upcoming
