1.
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d").date()
today = date.today()

age = relativedelta(today, birthdate)

print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")

2.
from datetime import datetime, date, timedelta

birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d").date()
today = date.today()

this_year_birthday = birthdate.replace(year=today.year)

if this_year_birthday < today:
    next_birthday = birthdate.replace(year=today.year + 1)
else:
    next_birthday = this_year_birthday

days_remaining = (next_birthday - today).days

print(f"Your next birthday is in {days_remaining} day(s).")


3.
from datetime import datetime, timedelta

current_input = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
current_datetime = datetime.strptime(current_input, "%Y-%m-%d %H:%M")

hours = int(input("Enter the meeting duration (hours): "))
minutes = int(input("Enter the meeting duration (minutes): "))

duration = timedelta(hours=hours, minutes=minutes)
end_time = current_datetime + duration

print(f"The meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")
4.

from datetime import datetime
import pytz

input_dt = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
from_tz = input("Enter your current timezone (e.g., 'US/Eastern'): ")
to_tz = input("Enter the target timezone (e.g., 'Asia/Tokyo'): ")

naive_dt = datetime.strptime(input_dt, "%Y-%m-%d %H:%M")

from_timezone = pytz.timezone(from_tz)
to_timezone = pytz.timezone(to_tz)

localized_dt = from_timezone.localize(naive_dt)
converted_dt = localized_dt.astimezone(to_timezone)

print(f"The time in {to_tz} is: {converted_dt.strftime('%Y-%m-%d %H:%M')}")

5.from datetime import datetime
import time

target_input = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")
target_time = datetime.strptime(target_input, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = target_time - now

    if remaining.total_seconds() <= 0:
        print("⏰ Time's up!")
        break

    print(f"\rTime remaining: {remaining}", end="")
    time.sleep(1)
6.
import re

email = input("Enter an email address: ")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("✅ Valid email address.")
else:
    print("❌ Invalid email address.")
7.
phone = input("Enter a 10-digit phone number: ")

digits = ''.join(filter(str.isdigit, phone))

if len(digits) == 10:
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    print("Formatted phone number:", formatted)
else:
    print("❌ Invalid input. Please enter exactly 10 digits.")
8.
import re

password = input("Enter a password: ")

length_ok = len(password) >= 8
has_upper = re.search(r'[A-Z]', password)
has_lower = re.search(r'[a-z]', password)
has_digit = re.search(r'\d', password)

if length_ok and has_upper and has_lower and has_digit:
    print("✅ Strong password.")
else:
    print("❌ Weak password. Make sure it:")
    if not length_ok:
        print("- Has at least 8 characters")
    if not has_upper:
        print("- Contains at least one uppercase letter")
    if not has_lower:
        print("- Contains at least one lowercase letter")
    if not has_digit:
        print("- Contains at least one digit")
9.
import re

sample_text = """
Python is a powerful programming language. Many developers love Python 
because it is easy to read and write. Python can be used for web development, 
data science, automation, and more.
"""

word = input("Enter a word to search for: ")

matches = list(re.finditer(rf'\b{re.escape(word)}\b', sample_text, re.IGNORECASE))

if matches:
    print(f"✅ Found '{word}' {len(matches)} time(s):")
    for match in matches:
        print(f"- At index {match.start()} to {match.end()}: \"{match.group()}\"")
else:
    print(f"❌ The word '{word}' was not found in the text.")
10.
import re

text = input("Enter text containing dates: ")

date_pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[./-]\d{1,2}[./-]\d{1,2})\b'

dates = re.findall(date_pattern, text)

if dates:
    print("✅ Dates found in the text:")
    for d in dates:
        print(f"- {d}")
else:
    print("❌ No dates found in the text.")


