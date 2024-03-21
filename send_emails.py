import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_birthday_emails(today_birthdays):
    # Read Excel sheet
    df = pd.read_excel('employees.xlsx')  # Replace 'employees.xlsx' with the path to your Excel file
    
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Gmail SMTP port
    sender_email = 'your@gmail.com'  # Your Gmail email address
    sender_password = '*** **** ***** *****'  # Your Gmail password
    
    # Login to Gmail SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    
    # Send birthday emails
    for index, row in today_birthdays.iterrows():
        recipient_email = row['Email']
        subject = 'Happy Birthday!'
        message = f"Dear {row['Employee Name']},\n\nWishing you a very happy birthday!\n\nBest regards,\nPowerCloud"
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        server.send_message(msg)
        print(f"Birthday email sent to {recipient_email}")
    
    # Logout from SMTP server
    server.quit()
