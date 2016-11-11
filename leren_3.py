
print('Wie bent u?')
ik = input()


teamlid_1 = 'JAN'
teamlid_2 = 'PETER'
teamlid_3 = 'GOZAg'

#het team, is een LIJST van teamleden
#een lijst is ook een "type variabele"

team = [teamlid_1, teamlid_2, teamlid_3]

print(team)


# met lijsten kun je leuke dingen
# stel dat ik iedereen in het team hun naam wil laten noemen
# ik kan doen:

print(teamlid_1)
print(teamlid_2)
print(teamlid_3)

# maar je wil niet voor elk teamlid een fking print schrijven.
# wat je kan doen met lijsten. is

# ITEREREN
url_iteratie_wikipedia = 'https://nl.wikipedia.org/wiki/Iteratie'
print('ITEREREN: ', url_iteratie_wikipedia)


# stel dat ik iedereen in het team hun naam wil laten noemen

for naam in team:
    print(naam)



