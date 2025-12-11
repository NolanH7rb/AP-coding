from helperfunction import plot_position_stat_bar , get_player_stats , dataframe_to_png ,  export_player_season_png , plot_player_stat_by_week
import matplotlib.pyplot as plt

#   Question 1
plot_position_stat_bar(2024, "QB", "passing_yards", save_path="qb_passingg_2024.png", top_n=25)

UnderRatedorOverRated = '3 Stats to detetmmine this!'
# Passing Yards
# Completion Percentage
# Points Scord before and after person was named starter
'Geno Smith'

Answer = ' Geno Smith is actually underated Quarterback according to my research and analysis. ' \
' One reason being through the 2022-2024 season Geno smith has stayed within the top 18 Quarterbacks ' \
' despite his backlash of his "incapable" performance and role as a starting quarterback. '

' Another stat we looked into was his completetion percedntage and in 2024 he had an average completion percentage '
' of %70.4, in 2023 he had a completion percentage of %64.7, and in 2022 he had a completion percentage of %69.9. '
' Through all three seasons he had a average of %67.4 which goes to show he is actually doing a good job as their starting quarter back thats not being valued enough. '

'Lastly we took a look at team he was on points per game before and after Geno Smtih was made quarter back. It seems in 2021 the team averaged 23.2 PPG while in 2022'
' when Geno was named starter their PPG went up to approxamately 24.0 PPG, Although it doesnt seem like much it shows the slow but progressive improvement of the team with Geno on it'
' in just one season. On top of that in the 2022 season his team finished with a record of 9-8 which is positive after coming from a rough 7-10 record the previous season.'
print(Answer)

playerData= get_player_stats(2024, 'Geno','Smith')
print(playerData)
