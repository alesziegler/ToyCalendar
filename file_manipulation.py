class FileManipulation:
  

  def __init__ (self, file):
    self.__file = file
  
  def delete_empty_lines(self):
    with open(self.__file, 'r',encoding = 'utf-8') as input:
      lines = input.readlines() #it works (type is list)
    #print(type(lines))
  
    non_empty_lines = []

    for line in lines:
      if line.strip() != "":
        non_empty_lines.append(line)

    return non_empty_lines
  
  """
  def make_lower_level_list_if_item_contains_given_character
  ok, problem is that this operation should follow deleting empty lines.

  """
  
  def combine_with_another_file_as_csv(self,another_file):
    list_of_names = self.delete_empty_lines()
    """
    Ok, maybe we should have a dictionary?
    """