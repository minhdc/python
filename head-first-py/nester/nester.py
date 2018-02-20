
def print_lol(the_list,ident = False, level = 0, place = sys.stdout):
    """
        print a list of (possibly) nested list
        - this function takes a positional arg <the_list>: which is any python list
        - a 2nd arg <ident_number> ; control wherether or not identation is shown on the display
        - a 3rd arg <level> is used to insert tab-stops when a nested list in encountered
        - a 4th arg <place> : is where to write the output
    """

    for element in the_list:
        if isinstance(element,list):
            print_lol(element,ident,level+1,place)
        else:
            if ident:
                for tab_stop in range(level, place):
                print("\t",end='',place)
            print(element,place)
