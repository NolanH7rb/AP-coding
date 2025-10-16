import pandas as pd
import nfl_data_py as nfl

from helperfunction import get_team_records, get_season_Results_By_team

#schedules = nfl.import_schedules([2024])

#print(schedules.columns.tolist())
#print(records[['team','wins','losses']])
#print(records[['wins']].mean())
records = get_team_records(2025)


#find a season where the average wins was below 8.5 ?


#Find a team that have averagle atleast 12 wins over the past 5 seasons.

birds = get_season_Results_By_team(2025, 'IND')
print(birds)
#pd[4, 3, 7, 6, -4, -17]
