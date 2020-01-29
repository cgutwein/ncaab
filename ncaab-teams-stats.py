from sportsreference.ncaab.teams import Teams
import pandas as pd

df_all = pd.DataFrame()
teams = Teams()
for team in teams:
    df_temp = team.dataframe
    df_all.append(df_temp)

df_all.to_csv('./team_stats.csv')
