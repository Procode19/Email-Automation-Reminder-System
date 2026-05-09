import os
import pandas as pd
import smtplib
from email.message import EmailMessage
import schedule
import time
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(filename='logs/email_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
CONTACTS_CSV = 'data/contacts.csv'
REMINDERS_CSV = 'data/reminders.csv'
TEMPLATE_FILE = 'templates/email_template.txt'
REPORT_CSV = 'outputs/email_report.csv'

def load_contacts():
    """Load contacts from CSV."""
    try:
        df = pd.read_csv(CONTACTS_CSV)
        return df.to_dict('records')
    except FileNotFoundError:
        logging.error("Contacts CSV not found.")
        return []

def load_reminders():
    """Load reminders from CSV."""
    try:
        df = pd.read_csv(REMINDERS_CSV)
        return df.to_dict('records')
    except FileNotFoundError:
        logging.error("Reminders CSV not found.")
        return []

def load_template():
    """Load email template."""
    try:
        with open(TEMPLATE_FILE, 'r') as f:
            return f.read()
    except FileNotFoundError:
        logging.error("Email template not found.")
        return ""

def personalize_email(template, contact):
    """Personalize email template with contact data."""
    return template.format(**contact)

def send_email(to_email, subject, body, dry_run=False):
    """Send email via SMTP."""
    if dry_run:
        logging.info(f"DRY RUN: Would send email to {to_email} with subject '{subject}'")
        return True, None

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = os.getenv('EMAIL_USER')
    msg['To'] = to_email

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
        server.send_message(msg)
        server.quit()
        logging.info(f"Email sent to {to_email}")
        return True, None
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {str(e)}")
        return False, str(e)

def schedule_reminders(reminders, contacts, template, dry_run=False):
    """Schedule reminders."""
    contact_dict = {c['email']: c for c in contacts}

    for reminder in reminders:
        contact_email = reminder['email']
        if contact_email not in contact_dict:
            logging.warning(f"Contact {contact_email} not found.")
            continue

        contact = contact_dict[contact_email]
        subject = reminder.get('subject', 'Reminder')
        body = personalize_email(template, contact)
        scheduled_time = reminder['scheduled_time']  # Assume format 'HH:MM'

        def job():
            success, error = send_email(contact_email, subject, body, dry_run)
            # Log to report
            with open(REPORT_CSV, 'a') as f:
                f.write(f"{datetime.now()},{contact_email},{subject},{'Sent' if success else 'Failed'},{error or ''}\n")

        # For simplicity, schedule daily at the time
        schedule.every().day.at(scheduled_time).do(job)

def main(dry_run=False):
    """Main function."""
    contacts = load_contacts()
    reminders = load_reminders()
    template = load_template()

    if not contacts or not reminders or not template:
        logging.error("Missing data. Check CSV files and template.")
        return

    # Initialize report
    with open(REPORT_CSV, 'w') as f:
        f.write("Timestamp,Email,Subject,Status,Error\n")

    schedule_reminders(reminders, contacts, template, dry_run)

    # Run scheduler
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Run in dry-run mode')
    args = parser.parse_args()
    main(dry_run=args.dry_run)