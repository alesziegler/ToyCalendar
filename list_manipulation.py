class ListManipulation:

    def __init__(self, input):
        if type(input) is list:
            self.__list = input
        else:
            raise ValueError
            
    def split_item_if_it_contains_given_separator_into_lower_level_list(self,separator):
        output = []
        for i in self.__list:
            if separator in i:
                lower_list = i.rsplit(separator)
                output.append(lower_list)
            else:
                output.append(i)
        return output
        