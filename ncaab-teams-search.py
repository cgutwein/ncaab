from sportsreference.ncaab.teams import Teams

for team in Teams():
    print(team.name, team.dataframe)
