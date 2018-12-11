# Eftirfarandi tafla sýnir þrjár dagsetningar og nafn viðkomandi frídaga:
 
# January 1 => New year's day
# June 17 => National holiday
# December 25 => Christmas day
 
# Skrifið forrit sem les inn nafn mánaðar og númer dags. Gera má ráð fyrir því að nafn mánaðar sé slegið inn í lágstöfum.
# Úr þessu inntaki skal búa til streng sem inniheldur nafn mánaðarins, með fyrsta staf sem hástaf, ásamt númeri dagsins, með einu bili á milli.
 
# Ef umræddur strengur er frídagur þá skal prenta út nafn viðkomandi frídags miðað við töfluna að ofan.
# Ef umræddur strengur er ekki frídagur þá skal prenta út "Not a holiday".
# Inntak/úttak forritsins á að vera nákvæmlega eins og fram kemur í dæminu hér fyrir neðan.
# Hint: Notið capitalize() fallið.


month_str = input("Month: ") 
day = input("Day: ")

full_date = '{0} {1}'.format(month_str.capitalize(), day)
print(full_date)

if full_date == "January 1":
    print("New year's day")

elif full_date == "June 17":
    print("National holiday")

elif full_date == "December 25":
    print("Christmas day")

else:
    print("Not a holiday")