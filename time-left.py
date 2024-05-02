import argparse
from datetime import datetime, timedelta

def calculate_life_metrics(dob, life_expectancy):
    today = datetime.today().date()
    dob = datetime.strptime(dob, '%Y-%m-%d').date()
    life_expectancy_date = dob + timedelta(days=life_expectancy * 365)  # Approximate, ignoring leap years

    days_lived = (today - dob).days
    weeks_lived = days_lived // 7

    total_life_days = (life_expectancy_date - dob).days

    days_left = total_life_days - days_lived
    weeks_left = days_left // 7

    life_percentage_used = (days_lived / total_life_days) * 100
    
    return weeks_lived, weeks_left, life_percentage_used


def print_boxes(weeks_lived, weeks_left):
    return "[X] " * weeks_lived + "[ ] " * weeks_left


def main():
    parser = argparse.ArgumentParser(description='Calculate life metrics based on date of birth and life expectancy.')
    parser.add_argument('--date-of-birth', type=str, required=True, help='Your date of birth in YYYY-MM-DD format')
    parser.add_argument('--life-expectancy', type=int, required=True, help='Your life expectancy in years')
    parser.add_argument('--print-boxes', action="store_true", required=False, help='Print filled and empty boxes for visualisation')

    args = parser.parse_args()

    weeks_lived, weeks_left, life_percentage_used = calculate_life_metrics(args.date_of_birth, args.life_expectancy)

    if args.print_boxes:
        print(print_boxes(weeks_lived, weeks_left))
    else:
        print(f"You have lived about {weeks_lived} weeks, you might live about {weeks_left} more.")
        print(f"You have used {life_percentage_used:.2f}% of your estimated life expectancy.")

if __name__ == "__main__":
    main()
