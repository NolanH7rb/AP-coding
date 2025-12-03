from helperfunction import get_player_stats_by_name, plot_weekly_player_stats,plot_player_stat, get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats
import matplotlib.pyplot as plt


#Question 1
'Descrptive'
teamData = get_advanced_team_records
print(teamData)

#This is descriptive because its very straight to the point and only requires 1 answer.

Answer = 'This is the answer'
print('')

#Question 2
'Comparison'

wr=weeklyPlayerStats(2024,'WR')
print(wr)
adv =get_player_stats_by_name(2024,'J.Chase','WR')


print(adv)
bop =get_position_columns(2024,"WR")
print(bop)


plot_weekly_player_stats(2024, "WR", stat= "targets ", top_n=3, save_path="quick_datas.png" )

# None of the code was working because certain attributes weren't installed,
# although Jamaar Chase had the most recpetions even though his targets is unknown.



#Question
'Comparison'

# Attributes were working possible helper function error and was
#  stuck on question 2 for long period of time. It is comparison
#  because the key word "correlate" and time of possession is compared with wins.