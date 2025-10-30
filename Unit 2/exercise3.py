
from helperfunction import get_team_records, get_season_Results_By_team, weeklyPlayerStats

# NOTE = you will need to pass the position, year and week in as an agrument
# position example : quarterback = 'QB', runnerback = 'RB'

qb= weeklyPlayerStats(2024,'QB') 

print(qb)
# 1. Who are the top 5 quarterbacks by passing yards?
print('Jared Goff, Joe Burrow, Baker Mayfield, Patrick Mahomes, Lamar Jackson')
#  What’s their average completion percentage (cmp_pct)?
print('J.Goff = 71.329879 '   \
      'J.Burrow = 70.552147 '  \
      'B.Mayfield = 71.768707 ' \
      'P.Mahomes = 67.319277 '   \
      'L.Jackson = 67.307692 '  )

# 2. What might a high cmp_pct tell you about a quarterback’s style of play?
print('A high completion percentage indicates the quarterback;s aggressive'  \
' and risky or safe playstyle during in game performance. For example they'   \
' completion could be high because of the number of short route or checkdowns' \
' they throw to play it safe or the low number of completion due to the gamble' \
' of threowing deep balls for 60+ yards to their reciever for the touchdown'     )


rb= weeklyPlayerStats(2024,'RB') 

print(rb)
# 3. Which RB had the highest rushing yards that week? Who had the best yards per carry (rush_ypc)?
print('Saquon had the highest rushing yards of the season.' \
      'Derrick Henry had the most yards per carry')


# 4. If a RB has high rush_yards but low rush_ypc, what could that mean? 
print('It could possibly mean that the RB requires more carries to get' \
      ' high amounts of yards and doesnt break out as often for the long run')

wr=weeklyPlayerStats(2024,'WR')
print(wr)
# 5. Find a player who has the best recieving yards on the fewest pass targets
print('Ladd McConkley')