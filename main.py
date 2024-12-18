from datetime import date, datetime, timedelta
from file_manipulation import FileManipulation

start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)
delta = end_date - start_date

# in this, list being comprehrended appears to be just list of numbers from 1 to 365 or 366.
# Operation consists in setting default date to appear in a new list and then adding to it
# number of days specified by an item in a list being comprehended.
# No names thus appear in a new list:
calendar = [(start_date + timedelta(days=item+1)).strftime("%d %B") for item in range(delta.days)]

#print(calendar)

"""
for i in range(delta.days):
  # in function, this maybe needs a list comprehension?
  print( (start_date + timedelta(days=i+1)).strftime("%d %B") )
"""
test_file_manip = FileManipulation("svatky.txt")

names = test_file_manip.delete_empty_lines()



#ok, lets do it differently - here we use matching indexes of our two lists

current_day = datetime.now().date().strftime("%d %B")

#print(current_day)

matching_index = calendar.index(current_day)

#print(matching_index)

current_name = names[matching_index+1]

print(f"Dnes ma svatek: {current_name}")



name = input("Zadejte sve jmeno: ")

try:
    #print(name)
    # if 
    matching_index = names.index(name.strip() + "\n")
    print("try")
except Exception as e:
    #print(e)
    print("Toto jméno není v kalendáři")

my_date = calendar[matching_index - 1]

print(f"Svatek mate {my_date}")

print(names[55])

print(names.index("Liliana\n"))

"""
Ok, we need something like if datetime.now().date() converted to an appropriate format
equals value in a dictionary, print keys?

Ok, we need a method that copies file and deletes empty lines from it.
Next, what?
We need to combine result of that method applied to our file, with 
calendar generated by other method.
Then we need way to retrieve data from this combination in a right way
"""

