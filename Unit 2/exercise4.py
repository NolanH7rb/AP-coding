from helperfunction import weeklyPlayerStats, plot_weekly_player_stats, plot_player_stat
import matplotlib.pyplot as plt

# 1) Using an existing stats dataframe:
stats = weeklyPlayerStats(2024, "QB")  
plot_player_stat(stats, stat="passing_tds", top_n=20, title=" Passing Touchdowns (2024)", save_path="QB_passing_tds_2024.png"  )

# 2) One-liner wrapper:
plot_weekly_player_stats(2024, "QB", stat="rushing_yards", top_n=3, week=[17], save_path="QB_rush_yards_wk17.png")

# Use the new plot_player_stat() and plot_weekly_player_stats() to visualize the data into bar graphs and answer the following questions.

# 1. Use each helper function to find your own metric to visualize. use the weeklyPlayerStats function to find positions and stat columns by name
print('Found out that the tight end(TE) leading in recieving yards is Brock bowers using the top 7 recieving stats for TE metric graph')

# 2. Find the player with the most touchdowns in 2024?
print('Derrick Henry and James Cook are tied for the most All-time touchdown in 2024')

# 3. Find the player with the higest total passing yards in 2024.
print('Lamar Jackson led the league in total passing touchdowns in 2024')

# 4. which player had the highest rushing yards in week 1 and in week 17?
print('Joe Mixon led the league in rushing yards in week 1 while Saquon had the highest rushing yards in week 17.')