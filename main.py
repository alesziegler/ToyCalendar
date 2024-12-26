from datetime import date, datetime, timedelta
from file_manipulation import FileManipulation
from list_manipulation import ListManipulation

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

#this part is testing:

test_list = ["hdash","cjpsjc","jfdojd,sdsdds"]

test_list_manip = ListManipulation(test_list)

deepened_test_list = test_list_manip.split_item_if_it_contains_given_separator_into_lower_level_list(",")

print(deepened_test_list)

test_list_to_dictionary_manip = ListManipulation(deepened_test_list)

test_dictionary_from_deepened_list = test_list_to_dictionary_manip.create_dictionary_of_lower_level_lists()

print(test_dictionary_from_deepened_list)

#Here testing ends. First empty lines are deleted and at the same time txt is converted into a list:

svatky_file_manip = FileManipulation("svatky.txt")

names = svatky_file_manip.delete_empty_lines()

#This takes names list, and returns list which has lower level lists in days with multiple names:

list_manip_names = ListManipulation(names)

more_names_in_one_day_in_lower_level_lists = list_manip_names.split_item_if_it_contains_given_separator_into_lower_level_list(",")

#this creates a dictionary where keys are names which share a date with another name and values are their indexes:

list_manip_more_names_in_one_day_in_lower_level_lists = ListManipulation(more_names_in_one_day_in_lower_level_lists)

dict_with_special_days = list_manip_more_names_in_one_day_in_lower_level_lists.create_dictionary_of_lower_level_lists()

print(dict_with_special_days)

#matching current day with calendar and retrieving index of relevant calendar date as an index:

current_day = datetime.now().date().strftime("%d %B")

matching_index = calendar.index(current_day)

#Reaching into names lists and comparing index there with calendar index retrieved in previous step:

current_name = names[matching_index+1]

print(f"Dnes ma svatek: {current_name}")

#

input_name = input("Zadejte sve jmeno: ")

try:
    #print(name)
    # if 
    matching_index = names.index(input_name.strip() + "\n")
    #somewhere here should be a if type list, do operation on a list
    #NO. Matching indexes for list-names should be stored in a special place somewhere
    print("try")
    my_date = calendar[matching_index - 1]
    print(f"Svatek mate {my_date}")
except Exception as e:
  there_is_a_match = False
  """
  We need a loop that will get through keys of a dictionary,
  and if it finds value corresponding to input name,
  then get its key and match it with calendar
  """
  for name in dict_with_special_days.keys():
    if name == input_name.strip():
       matching_index = dict_with_special_days.get(name)
       my_date = calendar[matching_index - 1]
       there_is_a_match = True
       print(f"Svatek mate {my_date}")
  if there_is_a_match is False:
    print("Toto jméno není v kalendáři")

#my_date = calendar[matching_index - 1]

#print(f"Svatek mate {my_date}")

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

