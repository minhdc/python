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


class Athlete:
    def __init__(self,ath_name, ath_dob = None, ath_times = []):
        self.name = ath_name
        self.dob = ath_dob
        self.times = ath_times

    def top_three_records(self):
        return sorted(set(sanitize(t) for t in self.times))[0:3]

    def add_times(self, ath_times=[]):
        self.times.extend(ath_times)

    def add_time(self, ath_time):
        self.times.append(ath_time)


class AthleteList(list):
    def __init__(self,ath_name,ath_dob=None,ath_times = []):
        list.__init__([])
        self.name = ath_name
        self.dob = ath_dob
        self.extend(ath_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        ath_data = data.strip().split(',')
        return (AthleteList(templ.pop(0), templ.pop(0), ath_data))
    except IOError as err:
        print('File Error ',str(err))
        return (None)
