import cgi
import athletemodel
import yate
import cgitb

# just enable CGI tracking in urgent case..
#cgitb.enable()

athletes = athletemodel.get_from_store()
#grab all of the form data and put it in a dir
form_data = cgi.FieldStorage()
ath_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing data"))
print(yate.header("Athlete : "+ath_name+", DOB : "+athletes[ath_name].dob+"."))
print(yate.para("The top 3 times for this ath are: "))
print(yate.u_list(athletes[ath_name].top3))

print(yate.include_footer({"Home":"/index.html","select another athletes":"generate_list.py"}))
