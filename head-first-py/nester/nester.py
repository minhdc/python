
def print_lol(the_list,ident_number):
    """this func takes an arg called 'the_list' which is any Python list data struct. 
    then print each of its element"""
    for element in the_list:
        if isinstance(element,list):
            print_lol(element,ident_number+1)
        else:
            for i in range(ident_number):
                print("\t",end='')
            print(element)



