
def sanitize(time_as_string):
    '''
        convert anykind of time format into mm.ss
    '''
    if '-' in time_as_string:
        splitter = '-'
    elif ':' in time_as_string:
        splitter = ':'
    else:
        return time_as_string
    (mins,secs) = time_as_string.split(splitter)
    return (mins + '.' + secs)


def get_unique_list_of(target_list):
    '''
        convert from list to unique_list (set)
    '''
    unique_elements = []
    for element in target_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements


def get_coach_data(input):
    '''
        get data in various format from coach
    '''
    output = []
    try:
        with open(input) as input_data:
            output = input_data.readline().strip().split(',')
    except IOError as err:
        print(err)
        return None
    return output


def convert_athlete_data_to_dict(data_as_list):
    data_as_dict = {}
    data_as_dict['name'] = data_as_list.pop(0)
    data_as_dict['dob'] = data_as_list.pop(0)
    data_as_dict['record'] = data_as_list
    return data_as_dict


sarah = convert_athlete_data_to_dict(get_coach_data('sarah2.txt'))

print(sarah['name'],"'s fastest records are : ",sorted(set(sanitize(t) for t in sarah['record']))[0:3])
