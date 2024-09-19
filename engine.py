from datetime import date, timedelta

start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)
delta = end_date - start_date

for i in range(delta.days):
  # in function, this maybe needs a list comprehension?
  print( (start_date + timedelta(days=i+1)).strftime("%d %B") )

def create_calendar_without_a_year(start_date, end_date):
  pass