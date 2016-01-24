from __future__ import division
from operator import itemgetter
import numpy
import nflgame

guess = 'NYJ'
curr = 18 

teams = ["PIT", "BAL", "CIN", "CLE", "NE", "BUF", "MIA", "NYJ", "TEN", "JAC",
     "IND", "HOU", "DEN", "KC", "SD", "OAK", "GB", "DET", "MIN", "CHI", 
     "DAL", "WAS", "PHI", "NYG", "ATL", "CAR", "NO", "TB", "SF", "SEA", 
     "ARI", "STL"]
rush_d = []
pass_d = []
for i in range(0,32):

# Query data for games from weeks 1 - curr for one team's season results
    games = nflgame.games(2015, week = range(1,curr), away = teams[i],
         home = teams[i])
# Combine the stats for the players in the games
    players = nflgame.combine_game_stats(games)

    passed = 0
    touch  = 0
# Calculate passing yards
    for p in players.passing().sort('passing_yds').limit(40):
        
        if p.team  != teams[i]:

            passed = passed + p.passing_yds
            touch  = touch  + p.passing_tds
    
    defense = "There were %d passing yards allowed for %s's defense"
#    print defense % (passed, teams[i])
    pass_per_game = passed/160
    touch_per_game = (touch*6)/16
    score = pass_per_game + touch_per_game
    if teams[i] == guess:
        total_pass = score
        print total_pass
        print ("LOOK HERE MAN!!!")
    pass_d.append([teams[i],score])

    
    rushed = 0
    touch = 0
# Calculate rushing yards
    for p in players.rushing().sort('rushing_yds').limit(40):
        
        if p.team  != teams[i]:

            rushed = rushed + p.rushing_yds
            touch  = touch  + p.rushing_tds
    
    defense = "There were %d rushing yards allowed for %s's defense"
 #   print defense % (rushed, teams[i])
    defense = "There were %d passing yards allowed for %s's defense"
  #  print defense % (touch, teams[i])
    rushed_per_game = rushed/640
    touch_per_game = (touch*3)/16
    score = rushed_per_game + touch_per_game
    rush_d.append([teams[i],score])
    

if type(teams[i] is str):
    print teams[i]


pass_d = sorted(pass_d, key=itemgetter(1))    
rush_d = sorted(rush_d, key=itemgetter(1))    
#print pass_d
#print rush_d


for i in range(0,32):
    if rush_d[i][0] == guess:
        print rush_d[i][1]
        defense = "The %s rush defense is ranked %d"
        print defense % (guess, i+1)
        print (i+1)


weeks = 0
# Stratify passing options, limit to main four options
strat = numpy.array([0,0,0,0])
strat = strat.astype(float)
for i in range(1,curr):
# Query game data, one game per week for 16 weeks
    game = nflgame.one(2015, i, guess, guess)
# Compile player data for a game

    try:

        game.players.passing()

    except AttributeError:
        continue     

    opp   = 0
    yards = 0
    week_strat = numpy.array([0,0,0,0])
    week_strat = week_strat.astype(float)
# Sort and run for best receiving results
    for p in game.players.receiving().sort("receiving_yds"):

        if p.team != guess:
            week_strat[opp] = p.receiving_yds
            opp       += 1

        if opp == 4:
# get out of this loop
            break

    for p in game.players.passing():
        
        if p.team != guess:

            yards     += p.passing_yds 
    
    week_strat /= yards
    strat      += week_strat
    weeks       = weeks +1


strat /= (curr - 1)
strat *= total_pass

print strat
