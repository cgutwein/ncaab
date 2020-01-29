from sportsreference.ncaab.boxscore import Boxscore

game_data = Boxscore('2018-04-02-21-villanova')
print(game_data.home_points)  # Prints 79
print(game_data.away_points)  # Prints 62
df = game_data.dataframe  # Returns a Pandas DataFrame of game metrics

## access individual players
for player in game_data.away_players:
    print(player.name, player.player_id, player.points, player.minutes_played)

## Output: 
# Muhammad-Ali Abdur-Rahkman muhammad-ali-abdur-rahkman-1 23 34
# Zavier Simpson zavier-simpson-1 10 34
# Moritz Wagner moritz-wagner-1 16 33
# Charles Matthews charles-matthews-1 6 33
# Isaiah Livers isaiah-livers-1 0 20
# Duncan Robinson duncan-robinson-1 0 22
# Jordan Poole jordan-poole-1 3 10
# Jon Teske jon-teske-1 2 7
# Jaaron Simmons jaaron-simmons-1 0 3
# Eli Brooks eli-brooks-1 0 3
# Ibi Watson ibi-watson-1 2 1
# Austin Davis austin-davis-1 0 0
# C.J. Baird cj-baird-1 0 0
