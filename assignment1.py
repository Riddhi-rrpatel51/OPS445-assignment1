#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
The python code in this file is original work written by
"Riddhi Patel". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: Riddhi Ritesh Patel
Semester: Fall 2024
Description: A script to calculate past and future dates by a specified number of days.
'''

import sys

def leap_year(year: int) -> bool:
    """Return True if the specified year is a leap year, otherwise False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month:int, year:int) -> int:
    """Returns the maximum days in a month for a given year (considering leap years)."""
    if month == 2:  # February
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:  # All other months
        return 31

def after(date: str) -> str:
    """
    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function works for years after 1582.
    """
    year, month, day = (int(x) for x in date.split('-'))
    day += 1  # move to the next day
    if day > mon_max(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1

    return f"{year}-{month:02}-{day:02}"

def before(date: str) -> str:
    """Return the date for the previous day of the given date in YYYY-MM-DD format."""
    year, month, day = (int(x) for x in date.split('-'))
    day -= 1  # move to the previous day

    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = mon_max(month, year)

    return f"{year}-{month:02}-{day:02}"

def usage():
    """Print a usage message to the user."""
    print("Usage:", sys.argv[0], "YYYY-MM-DD NN")
    sys.exit(1)

def valid_date(date: str) -> bool:
    """Check if a date in 'YYYY-MM-DD' format is valid."""
    try:
        # Split the date string and convert parts to integers
        year, month, day = map(int, date.split('-'))

        # Check if the year has four digits
        if not (1000 <= year <= 9999):
            print(f"Invalid year: {year}")
            return False
        # Validate month range
        if not (1 <= month <= 12):
            print(f"Invalid month: {month}")
            return False

        # Get maximum days in the month for the specified year
        max_day = mon_max(month, year)

        # Validate day is within the valid range for the month
        if not (1 <= day <= max_day):
            print(f"Invalid day: {day}")
            return False

        # All checks passed, date is valid
        return True

    except (ValueError, AttributeError) as e:
        # If date format is incorrect or split fails, return False
        print(f"Error encountered: {e}")
        return False

def dbda(start_date: str, step: int) -> str:
    """
    Given a start date and a number of days (step), return the date that
    is `step` days into the past or future.
    """
    date = start_date
    if step > 0:
        for _ in range(step):
            date = after(date)
    else:
        for _ in range(-step):
            date = before(date)
    return date

if __name__ == "__main__":
    # Process command-line arguments
    if len(sys.argv) != 3:
        usage()
    
    start_date = sys.argv[1]
    try:
        divisor = int(sys.argv[2])
    except ValueError:
        usage()

    # Validate date and divisor
    if not valid_date(start_date) or divisor == 0:
        usage()

    # Calculate number of days based on divisor
    days = round(365 / divisor)
    print(f"A year divided by {divisor} is {days} days.")
    
    # Calculate past and future dates
    past_date = dbda(start_date, -days)
    future_date = dbda(start_date, days)
    
    print(f"The date {days} days ago was {past_date}.")
    print(f"The date {days} days from now will be {future_date}.")
