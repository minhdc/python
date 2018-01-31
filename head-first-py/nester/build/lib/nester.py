
def print_lol(the_list):
    """this func takes an arg called 'the_list' which is any Python list data struct. 
    then print each of its element"""
    for element in the_list:
        if isinstance(element,the_list):
            print_lol(element)
        else:
            print(element)
