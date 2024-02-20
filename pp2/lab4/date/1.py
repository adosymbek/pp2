from datetime import datetime, timedelta

current_date = datetime.now()

five_days = timedelta(days=5)

new_date = current_date - five_days

print("Current Date:", current_date)
print("Date five days ago:", new_date)