from sportsreference.nfl.schedule import Schedule

houston_schedule = Schedule('HOU')
for game in houston_schedule:
    print(game.date, game.points_scored, game.points_allowed)
