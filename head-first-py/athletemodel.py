import pickle
from athletes import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        ath_data = data.strip().split(',')
        return (AthleteList(ath_data.pop(0), ath_data.pop(0),ath_data))
    except IOError as err:
        print("File Err: ",str(err))
        return None


def put_to_store(files_list):
    '''
        get a list of filename then return list of all athletes that need to be saved
    '''
    all_ath = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_ath[ath.name] = ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_ath,athf)
    except IOError as err:
        print('File error(put_and_store)',str(err))
    return (all_ath)


def get_from_store():
    all_athl = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athl = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store):',str(err))
    return (all_athl)
