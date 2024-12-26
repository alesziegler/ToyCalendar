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
        
    def create_dictionary_of_lower_level_lists(self):
        output = {}
        #ok, indexes in first-level list will be values(since they are repeated)
        #values in lower level lists will be keys
        #it only works for lists with non-repeated values
        for i in self.__list:
            if type(i) is list:
                for i_lower in i:
                    output.update({i_lower: self.__list.index(i)})
                    
        return output