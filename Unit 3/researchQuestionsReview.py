from helperfunction import get_player_stats_by_name, plot_weekly_player_stats,plot_player_stat, get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats
import matplotlib.pyplot as plt

# Columns available to research based on year and position
#columnData = get_position_columns(2024, "QB")
# print(columnData)

'1. How much does QB pass accuracy influence team wins ? '
#teamRecord = get_team_records(2024)
#print(teamRecord)

#qbData = weeklyPlayerStats(2024, 'QB')
#print(qbData)

'J.Allen'
'J.Hurts'

#playerStat= get_player_stats_by_name(2024,'J.Hurts','QB')
#print(playerStat)

'Answer: Yes, there is a relationship. based on the average qb completion %, anything above 60 % is considered a good completion number'
"also based on team records, the top 10- top teams all have had qbs that have over 65% completion percentages."


'2. Does defensive turnovers contribute to a teams win percentage ? '
adv =get_advanced_team_records(2024,'turnovers')

print(adv)
print('Yes, defensive turnovers do contribute to team win percentage according to the data.')

'3.Who has the most passing yards of all time ?'
#qbData = weeklyPlayerStats(2000-2024, 'QB')
#print(qbData)
#stats = weeklyPlayerStats(2024, "QB")  
#plot_weekly_player_stats(2024, "QB", stat="rushing_yards", top_n=3, year=[], save_path="QB_all-time_passingyards_.png")

#Answer
print('This question is too broad for the simple fact that its not measurable'
' or researchable. I tried to use the helper function through a dtata frame and graph.')