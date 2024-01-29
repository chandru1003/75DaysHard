import re
from datetime import datetime, timedelta
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the scopes for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

def validate_email(email):
    # Regular expression for validating email format
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

def validate_timing(time_str):
    # Regular expression for validating timing format (HH:MM AM/PM)
    timing_regex = r'^\d{1,2}:\d{2} (AM|PM)$'
    return re.match(timing_regex, time_str)

def get_user_info():
    name = input("Enter Your name: ")

    while True:
        email = input("Enter your Email ID: ")
        if validate_email(email):
            break
        else:
            print("Invalid email format. Please enter a valid email address")

    habits_count = int(input("How many habits do want to follow? "))
    day_count = int(input("Number of days you want to follow: "))
    habits = []
    timings = []

    for i in range(habits_count):
        habit = input(f"Enter the habit {i+1}: ")
        while True:
            time_str = input(f"Enter Timing for habit {i+1} (e.g., 07:00 AM): ")
            if validate_timing(time_str):
                timings.append(time_str)
                habits.append(habit)
                break
            else:
                print("Invalid Time format...")

    return name, email, habits, timings, day_count

def create_google_calendar_event(service, summary, start_datetime):
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Your timezone',
        },
        'end': {
            'dateTime': (start_datetime + timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Your timezone',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 30},
            ],
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

def main():
    print("Welcome to 75 Days Hard!")
    name, email, habits, timings, day_count = get_user_info()
    print(name)
    print(email)

    # Initialize Google Calendar API
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)

    start_date = datetime.now() + timedelta(days=1)  # Start from tomorrow

    for day in range(1, day_count + 1):
        print(f"List of habits to follow, Day - {day} ({start_date.strftime('%Y-%m-%d')}):")
        for i, habit in enumerate(habits):
            print(f"- {habit}: do it at {timings[i]}")
            # Convert timing to datetime object
            timing_datetime = datetime.combine(start_date, datetime.strptime(timings[i], "%I:%M %p").time())
            create_google_calendar_event(service, habit, timing_datetime)
        start_date += timedelta(days=1)  # Increment date for the next day
        print("---------------------------------------------------")
        print("\n")

if __name__ == "__main__":
    main()
