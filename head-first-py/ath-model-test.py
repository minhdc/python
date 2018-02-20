import athletemodel
the_files = ['sarah2.txt','james2.txt','mikey2.txt','julie2.txt']
data = athletemodel.put_to_store(the_files)

for ath in data:
    print(data[ath].name)
