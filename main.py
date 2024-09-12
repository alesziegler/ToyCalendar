import calendar
from datetime import date, timedelta

#def get_date_range(start_date, end_date):
start_date = date(2024, 2, 15)
end_date = date(2024, 3, 5)
delta = end_date - start_date
print(delta.days)
print(type(delta))
print(range(delta.days))
"""
  return [start_date + timedelta(days=i) for i in range(delta.days + 1)]

# Example usage:


date_range = get_date_range(start, end)

# Print the dates
for d in date_range:
    print(d.strftime("%Y-%m-%d"))

    """