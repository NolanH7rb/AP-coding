from helperfunction import plot_position_stat_bar , get_player_stats , dataframe_to_png ,  export_player_season_png , plot_player_stat_by_week
import matplotlib.pyplot as plt

#1
plot_position_stat_bar(2022, "RB", "rushing_yards", save_path="rb_rushing_2022.png", top_n=25)

print('According to the season record of 2022 through 2024 it seems it was close between' \
' Saquon Barkley and Derrick Henry for the lead rusher over the years but with the right' \
' estimate came to the conclusion that Saquon was the leading Running Back in rushing' \
' yards between the season given by a few yards. This question was also comparison because' \
' I had to compare the running backs rushing yards between each other to find out who ended up on top')

#2
plot_player_stat_by_week(2022 , 'Matthew' , 'Stafford' , 'passing_yards' , save_path="QB_passingyds_2022.png")
#bop = get_player_stats(2024 , 'Matthew' , 'Stafford')
#print(bop)

plot_position_stat_bar(2023, "QB", "passing_yards", save_path="qbbbb_rushing_2023.png", top_n=25)

print("I statred trying to use the line bar graph to find if Matthew Stafford Declined or Increases" \
" through the 2022-2024 season. Then it wasn't returning me the right stats so I switched the player"
" and got the stat the same way I did in question one. In result I used Joe burrow and found that he" \
" had around 5,000 passing yard in 2022, 2,000 passing yards in the 2023 season, and around 5,000 again" \
" in his 2024 season. In a spand of these years he averaged approximately 4,000 passing yards and I " \
" believe he approved through these years because data shows he was hurt in 2023 for most of the season" \
" which is why he didn't end near or higher than 5,000 passing yards")
