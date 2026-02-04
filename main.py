from datetime import datetime

# Завдання 1
def get_days_from_today(date):
    try:
        # дата отримана на вході
        in_date = datetime.strptime(date, "%Y-%m-%d")
    except:
        pass

    # Поточна дата
    current_date = datetime.today()
    
    # Розрахунок кількості днів
    return current_date.toordinal() - in_date.toordinal()

print (get_days_from_today('2026-02-01'))