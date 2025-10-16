# step 1 - import code libraries to help us
import nfl_data_py as nfl
import pandas as pd
import os
# step 2 - test path to make sure we are
# accessing the nfl csv data.
path = os.path.abspath('nflData/nfl_records_2024.csv')

records = pd.read_csv(path)
#print(records.head())
#print(records.columns)

# import team data
teams = nfl.import_team_desc()

# team_stats = nfl.import_injuries([2024])
# #print(team_stats.columns)
# wins = nfl.import_win_totals([])
# #bestRecord = team_stats.sort_values(by = 'wins' , ascending = False)
# print(wins.head())
import pandas as pd
import nfl_data_py as nfl

g = nfl.import_schedules([2025])
if "season_type" in g.columns: g = g[g["season_type"] == "REG"]
elif "game_type" in g.columns: g = g[g["game_type"] == "REG"]
g = g.dropna(subset=["home_score", "away_score"])

home = g[["home_team", "home_score", "away_score"]].rename(columns={"home_team":"team","home_score":"pf","away_score":"pa"})
away = g[["away_team", "away_score", "home_score"]].rename(columns={"away_team":"team","away_score":"pf","home_score":"pa"})
tg = pd.concat([home, away])

rec = (tg.assign(w=(tg.pf>tg.pa).astype(int), l=(tg.pf<tg.pa).astype(int), t=(tg.pf==tg.pa).astype(int))
         .groupby("team")[["w","l","t"]].sum().reset_index()
         .rename(columns={"w":"wins","l":"losses","t":"ties"})
         .sort_values(["wins","losses"], ascending=[False,True]))

teams = nfl.import_team_desc()
print(rec.merge(teams, left_on="team", right_on="team_abbr")[["team_name","wins","losses","ties"]].head(5))


##############################################################################################################################################################


g = nfl.import_schedules([2025])
if "season_type" in g.columns: g = g[g["season_type"] == "REG"]
elif "game_type" in g.columns: g = g[g["game_type"] == "REG"]
g = g.dropna(subset=["home_score", "away_score"])

home = g[["home_team", "home_score", "away_score"]].rename(columns={"home_team":"team","home_score":"pf","away_score":"pa"})
away = g[["away_team", "away_score", "home_score"]].rename(columns={"away_team":"team","away_score":"pf","home_score":"pa"})
tg = pd.concat([home, away])

rec = (tg.assign(w=(tg.pf>tg.pa).astype(int), l=(tg.pf<tg.pa).astype(int), t=(tg.pf==tg.pa).astype(int))
         .groupby("team")[["w","l","t"]].sum().reset_index()
         .rename(columns={"w":"wins","l":"losses","t":"ties"})
         .sort_values(["wins","losses"], ascending=[True ,False]))

teams = nfl.import_team_desc()
print(rec.merge(teams, left_on="team", right_on="team_abbr")[["team_name","wins","losses","ties"]].head(5))