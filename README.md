# Email Automation & Reminder System

## Project Overview
This is a Python-based email automation and reminder system that allows scheduling and sending automated emails (one-off or recurring), tracking delivery status, and firing personal/team reminders. It uses CSV for contacts and reminders, SMTP for email sending, and provides logging and reporting.

## Problem Statement
Manual email sending and reminder management is time-consuming and error-prone. This system automates repetitive communication tasks, ensuring timely reminders for meetings, deadlines, payments, etc., improving productivity for HR, sales, operations, and admin teams.

## Industry Relevance
- **HR Teams**: Onboarding reminders, deadline notifications.
- **Sales Teams**: Follow-up emails, meeting alerts.
- **Operations Teams**: Task notifications, payment reminders.
- **Educators/Trainers**: Class reminders, webinar notifications.

## Features
- Load contacts from CSV
- Load reminders from CSV
- Email template personalization
- SMTP email sending with Gmail
- Reminder scheduling (one-off and recurring)
- Logging of sent/failed emails
- CSV report generation
- Dry-run mode for testing
- Safe password handling with environment variables

## Tech Stack
- Python 3.8+
- smtplib, email.message for email sending
- schedule, datetime for scheduling
- pandas for CSV handling
- logging for logs
- dotenv for environment variables

## Folder Structure
```
Email-Automation-Reminder-System/
├── data/                 # CSV files for contacts and reminders
├── templates/            # Email template files
├── src/                  # Source code modules
├── outputs/              # Generated reports
├── logs/                 # Log files
├── images/               # Screenshots and images
├── docs/                 # Documentation
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore file
└── main.py               # Main script
```

## Setup Instructions
1. Clone or download the project.
2. Install Python 3.8+ if not installed.
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Set up environment variables: Copy `.env.example` to `.env` and fill in your Gmail credentials.

## Environment Variable Setup
Create a `.env` file in the root directory:
```
EMAIL_USER=yourgmail@gmail.com
EMAIL_PASS=yourapppassword
```

Note: Use Gmail App Password, not your regular password.

## How to Run
- Dry-run mode: `python main.py --dry-run`
- Actual send: `python main.py`

## Sample Output
- Logs in `logs/email_log.txt`
- Report in `outputs/email_report.csv`

## Screenshots
(Add screenshots here)

## Learning Outcomes
- Python scripting
- Email automation
- Scheduling
- CSV handling
- Logging and error handling
- Environment variables for security