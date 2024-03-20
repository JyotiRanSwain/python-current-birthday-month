from flask import Flask, render_template
from birthday import get_monthly_birthdays
from send_emails import send_birthday_emails
import schedule
import threading
import time

app = Flask(__name__)

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_birthdays')
def get_birthdays():
    past_birthdays, today_birthdays, upcoming_birthdays = get_monthly_birthdays('employees.xlsx')

    # Format birthday messages
    birthday_messages = []
    for _, row in today_birthdays.iterrows():
        birthday_messages.append(f"Happy birthday to {row['Employee Name']}!")

    return render_template('birthday_list.html', past_birthdays=past_birthdays, today_birthdays=today_birthdays, upcoming_birthdays=upcoming_birthdays, birthday_messages=birthday_messages)

# Function to send birthday emails
def send_birthday_emails_job():
    _, today_birthdays, _ = get_monthly_birthdays('employees.xlsx')
    send_birthday_emails(today_birthdays)

# Schedule email sending every day at 1:06 PM
schedule.every().day.at("00:01").do(send_birthday_emails_job)

# Run the scheduler in a separate thread
def scheduler_thread():
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    # Start the scheduler thread
    scheduler = threading.Thread(target=scheduler_thread)
    scheduler.start()

    # Run the Flask app
    app.run(host='0.0.0.0', debug=True)
