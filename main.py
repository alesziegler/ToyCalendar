from datetime import date, datetime
from file_manipulation import FileManipulation

print(datetime.now().date())

start_date = date(2024, 1, 1)

print(type(start_date))

test_file_manip = FileManipulation("svatky.txt")

"""
Ok, we need a method that copies file and deletes empty lines from it.
Next, what?
We need to combine result of that method applied to our file, with 
calendar generated by other method.
Then we need way to retrieve data from this combination in a right way
"""

