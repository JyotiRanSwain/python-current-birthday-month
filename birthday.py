import pandas as pd
from datetime import datetime

def get_monthly_birthdays(file_path):
    df = pd.read_excel(file_path)
    df['Birthday'] = pd.to_datetime(df['Birthday'], errors='coerce')
    today = datetime.now().date()
    current_month = today.month
    current_year = today.year
    this_month_birthdays = df[(df['Birthday'].dt.month == current_month) & (df['Birthday'].dt.year <= current_year)]
    past_birthdays = this_month_birthdays[this_month_birthdays['Birthday'].dt.day < today.day]
    today_birthdays = this_month_birthdays[this_month_birthdays['Birthday'].dt.day == today.day]
    upcoming_birthdays = this_month_birthdays[this_month_birthdays['Birthday'].dt.day > today.day]
    return past_birthdays, today_birthdays, upcoming_birthdays
