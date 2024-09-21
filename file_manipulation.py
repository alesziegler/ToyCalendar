class FileManipulation:
  

  def __init__ (self, file):
    self.__file = file
  
  def delete_empty_lines(self):
    with open(self.__file, 'r') as input:
      lines = input.readlines() #it works (type is list)
    print(type(lines))
  """
    non_empty_lines = []

    for line in lines:
      if line.strip() != "":
        non_empty_lines.append(line)
    print(non_empty_lines)
  
  
  def remove_empty_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
  
    non_empty_lines = [line for line in lines if line.strip() != ""]
  
    with open(output_file, 'w') as file:
        file.writelines(non_empty_lines)
  
  # Example usage
  input_file = "input.txt"
  output_file = "output.txt"
  remove_empty_lines(input_file, output_file)
  """
  
  def combine_with_another_file_as_csv(self,another_file):
    pass