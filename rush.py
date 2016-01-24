from __future__ import division

import nflgame 

curr = 18

# New England Patiots
# Query data for games from weeks 1-17 
games = nflgame.games(2015, week=range(1,curr), away = "NE", home ="NE")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)

# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
tom_brady = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'T.Brady':

    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for New England's Defense"
print defense % (passed)
defense = "There were %d passing yards allowed for New England's Defense"
print defense % (touch)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(80):

    if p.name != 'L.Blount' and p.name != 'D.Lewis' and p.name != 'B.Bolden' and p.name != 'T.Brady' and p.name != 'S.Jackson' and p.name != 'J.White' and p.name != 'J.Iosefa' and p.name != 'J.Garoppolo' and p.name != 'J.Edelman' and p.name != 'D.Amendola' and p.name != 'B.Lafell' and p.name != 'K.Martin':

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for New England's Defense"
print defense % (rushed)
defense = "There were %d rushing yards allowed for New England's Defense"
print defense % (touch)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score

## This is the J-E-T-S JETS! JETS! JETS!
games = nflgame.games(2015, week=range(1,curr), away = "NYJ", home ="NYJ")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'R.Fitzpatrick' and p.name != 'G.Smith':

    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for the Jet's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'C.Ivory' and p.name != 'B.Powell' and p.name != 'R.Fitzpatrick' and p.name != 'S.Ridley' and p.name != 'Z.Stacy' and p.name != 'G.Smith' and p.name != 'T.Bohanon':

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Jet's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score





## The Buffalo Losers


games = nflgame.games(2015, week=range(1,curr), away = "BUF", home ="BUF")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'T.Taylor' and p.name != 'E.Manuel' and p.name != 'C.Hogan':

        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Buffalo's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score

touch = 0;
rush = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'L.McCoy' and p.name != 'T.Taylor' and p.name != 'Ka.Williams' and p.name != 'M.Gillislee' and p.name != 'A.Dixon' and p.name != 'E.Manuel' and p.name != 'P.Harvin' and p.name != 'C.Wood' and p.name != 'C.Hogan' and p.name != 'J.Felton' and p.name != 'S.Watkins' and p.name != 'C.Schmidt' and p.name != 'R.Woods' and p.name != 'M.Thigpen':

#        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rush = rush + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Buffalo's Defense"
print defense % (rush)
rush_per_game = rush/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## The Miami Dolphins


games = nflgame.games(2015, week=range(1,curr), away = "MIA", home ="MIA")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'R.Tannehill' and p.name != 'M.Moore' and p.name != 'J.Landry':

#        print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Miami's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'L.Miller' and p.name != 'J.Ajayi' and p.name != 'R.Tannehill' and p.name != 'J.Landry' and p.name != 'D.Williams' and p.name != 'M.Moore' and p.name != 'R.Matthews':

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Miami's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score


## Dallas Cowboys
games = nflgame.games(2015, week=range(1,curr), away = "DAL", home ="DAL")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'T.Romo' and p.name != 'M.Cassel' and p.name != 'K.Moore' and p.name != 'D.McFadden' and p.name != 'B.Weeden':

#        print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Dallas's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score


touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'D.McFadden' and p.name != 'J.Randle' and p.name != 'R.Turbin' and p.name != 'M.Cassel' and p.name != 'L.Whitehead' and p.name != 'L.Dunbar' and p.name != 'T.Romo' and p.name != 'K.Moore' and p.name != 'J.Heath' and p.name != 'C.Michael':

#        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Dallas's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score


## Washington Redskins

games = nflgame.games(2015, week=range(1,curr), away = "WAS", home ="WAS")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'K.Cousins' and p.name != 'C.McCoy' and p.name != 'J.Crowder':

 #       print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Redskin's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'A.Morris' and p.name != 'M.Jones' and p.name != 'C.Thompson' and p.name != 'K.Cousins' and p.name != 'P.Thomas' and p.name != 'D.Young' and p.name != 'C.McCoy' and p.name != 'J.Crowder':

#        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Redskin's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score


## New York Giants

games = nflgame.games(2015, week=range(1,curr), away = "NYG", home ="NYG")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'E.Manning' and p.name != 'R.Nassib':

#        print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Giant's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'R.Jennings' and p.name != 'A.Williams' and p.name != 'S.Vereen' and p.name != 'O.Darkwa' and p.name != 'E.Manning' and p.name != 'D.Harris' and p.name != 'O.Beckham':

#        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for the Giant's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score


## Philadelphi Eagles

games = nflgame.games(2015, week=range(1,curr), away = "PHI", home ="PHI")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'S.Bradford' and p.name != 'M.Sanchez':

 #       print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Philadelphia's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'D.Murray' and p.name != 'R.Mathews' and p.name != 'D.Sproles' and p.name != 'K.Barner' and p.name != 'S.Bradford' and p.name != 'M.Sanchez':

#        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Philadelphia's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score


## Carolina Panthers

games = nflgame.games(2015, week=range(1,curr), away = "CAR", home ="CAR")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'C.Newton' and p.name != 'D.Anderson':

#        print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Carolina's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'J.Stewart' and p.name != 'C.Newton' and p.name != 'C.Newton' and p.name != 'M.Tolbert' and p.name != 'C.Artis-Payne' and p.name != 'F.Whittaker' and p.name != 'D.Anderson' and p.name != 'C.Brown' and p.name != 'T.Ginn' and p.name != 'J.Cotchery' and p.name != 'J.Webb' and p.name != 'B.Nortman':

#        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Carolina's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score




## Tampa Bay Buccaneers

games = nflgame.games(2015, week=range(1,curr), away = "TB", home ="TB")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'J.Winston':

#        print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Tampa Bay's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'D.Martin' and p.name != 'C.Sims' and p.name != 'J.Winston' and p.name != 'B.Rainey' and p.name != 'J.Lane':

#        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Tampa Bay's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## New Orleans Saints

games = nflgame.games(2015, week=range(1,curr), away = "NO", home ="NO")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'D.Brees' and p.name != 'L.McCown' and p.name != 'T.Cadet':

 #       print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for New Orleans Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'M.Ingram' and p.name != 'T.Hightower' and p.name != 'K.Robinson' and p.name != 'C.Spiller' and p.name != 'D.Brees' and p.name != 'B.Cooks' and p.name != 'T.Cadet' and p.name != 'A.Johnson' and p.name != 'K.Hunter' and p.name != 'M.Hoomanawanui':

#        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for New Orleans' Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score




## Atlanta Falcons

games = nflgame.games(2015, week=range(1,curr), away = "ATL", home ="ATL")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'M.Ryan' and p.name != 'S.Renfree':

    #    print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Atlanta's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'D.Freeman' and p.name != 'T.Coleman' and p.name != 'M.Ryan' and p.name != 'T.Ward' and p.name != 'E.Weems' and p.name != 'P.DiMarco' and p.name != 'S.Renfree':

   #     print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Atlanta's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## Minnesota Vikings

games = nflgame.games(2015, week=range(1,curr), away = "MIN", home ="MIN")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'T.Bridgewater' and p.name != 'S.Hill':

 #       print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Minnesota's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'A.Peterson' and p.name != 'J.McKinnon' and p.name != 'T.Bridgewater' and p.name != 'M.Asiata' and p.name != 'Z.Line' and p.name != 'A.Thielen' and p.name != 'S.Hill' and p.name != 'S.Diggs' and p.name != 'C.Patterson' and p.name != 'J.Wright' and p.name != 'M.Wallace' and p.name != 'J.Locke':

#        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Minnesota's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## Green Bay

games = nflgame.games(2015, week=range(1,curr), away = "GB", home ="GB")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'A.Rodgers' and p.name != 'S.Tolzien':

   #     print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Green Bay's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'E.Lacy' and p.name != 'J.Starks' and p.name != 'A.Rodgers' and p.name != 'R.Cobb' and p.name != 'J.Kuhn' and p.name != 'J.Crockett' and p.name != 'T.Montgomery' and p.name != 'S.Tolzien' and p.name != 'R.Rodgers' and p.name != 'T.Masthay':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Green Bay's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## Detroit Lions

games = nflgame.games(2015, week=range(1,curr), away = "DET", home ="DET")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'M.Stafford' and p.name != 'D.Orlovsky':

   #     print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Detroit's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'A.Abdullah' and p.name != 'J.Bell' and p.name != 'M.Stafford' and p.name != 'T.Riddick' and p.name != 'Z.Zenner' and p.name != 'G.Tate' and p.name != 'M.Burton' and p.name != 'G.Winn' and p.name != 'I.Abdul-Quddus' and p.name != 'T.Jones':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Detroit's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score


## Chicago Bears

games = nflgame.games(2015, week=range(1,curr), away = "CHI", home ="CHI")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'J.Cutler':

   #     print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Chicago's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'M.Forte' and p.name != 'J.Langford' and p.name != 'K.Carey' and p.name != 'J.Cutler' and p.name != 'J.Rodgers' and p.name != 'A.Smith' and p.name != 'E.Royal':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Chicago's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## San Francisco 49ers

games = nflgame.games(2015, week=range(1,curr), away = "SF", home ="SF")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'B.Gabbert' and p.name != 'C.Kaepernick':

   #     print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for San Francisco's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'C.Hyde' and p.name != 'S.Draughn' and p.name != 'C.Kaepernick' and p.name != 'M.Davis' and p.name != 'B.Gabbert' and p.name != 'D.Harris' and p.name != 'J.Hayne' and p.name != 'K.Gaskins' and p.name != 'R.Bush' and p.name != 'B.Miller' and p.name != 'B.Ellington' and p.name != 'Q.Patton':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for San Francisco's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## Seattle

games = nflgame.games(2015, week=range(1,curr), away = "SEA", home ="SEA")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'R.Wilson' and p.name != 'T.Jackson':

   #     print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Seattle's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

   # if p.name != 'T.Rawls' and p.name != 'M.Lynch' and p.name != 'R.Wilson' and p.name != 'C.Michael' and p.name != 'F.Jackson' and p.name != 'B.Brown' and p.name != 'D.Coleman' and p.name != 'T.Jackson' and p.name != 'T.Lockett' and p.name != 'W.Tukuafu' and p.name != 'K.Williams':
    if p.team != 'SEA':
    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Seattle's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score




## Arizona Cardinals

games = nflgame.games(2015, week=range(1,curr), away = "ARI", home ="ARI")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'C.Palmer' and p.name != 'D.Stanton':

   #     print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Arizona's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'C.Johnson' and p.name != 'D.Johnson' and p.name != 'A.Ellington' and p.name != 'K.Williams' and p.name != 'C.Palmer' and p.name != 'S.Taylor' and p.name != 'D.Stanton' and p.name != 'J.Brown' and p.name != 'J.Nelson':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Arizona's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## Los Angeles Rams

games = nflgame.games(2015, week=range(1,curr), away = "STL", home ="STL")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'N.Foles' and p.name != 'C.Keenum' and p.name != 'S.Mannion' and p.name != 'J.Hekker':

   #     print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Los Angeles' Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'T.Gurley' and p.name != 'T.Mason' and p.name != 'T.Austin' and p.name != 'B.Cunningham' and p.name != 'N.Foles' and p.name != 'C.Keenum' and p.name != 'M.Brown':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Los Angeles' Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## Indianapolis Colts

games = nflgame.games(2015, week=range(1,curr), away = "IND", home ="IND")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'A.Luck' and p.name != 'M.Hasselbeck' and p.name != 'C.Whitehurst' and p.name != 'Jo.Freeman' and p.name != 'R.Lindley':

  #      print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Indianapolis' Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'F.Gore' and p.name != 'A.Luck' and p.name != 'A.Bradshaw' and p.name != 'J.Robinson' and p.name != 'M.Hasselback' and p.name != 'D.Herron' and p.name != 'J.Freeman' and p.name != 'Z.Tipton' and p.name != 'P.Dorsett' and p.name != 'T.Williams' and p.name != 'C.Whitehurst' and p.name != 'P.McAfee' and p.name != 'T.Varga' and p.name != 'D.Allen' and p.name != 'J.Reitz' and p.name != 'C.Anderson':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Indianapolis' Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## Houston Texans

games = nflgame.games(2015, week=range(1,curr), away = "HOU", home ="HOU")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'B.Hoyer' and p.name != 'T.Yates' and p.name != 'B.Weeden' and p.name != 'B.Daniels' and p.name != 'C.Shorts' and p.name != 'J.Grimes' and p.name != 'R.Mallett':

  #      print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Houston's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'A.Blue' and p.name != 'C.Polk' and p.name != 'A.Foster' and p.name != 'J.Grimes' and p.name != 'A.Hunt' and p.name != 'B.Hoyer' and p.name != 'C.Shorts' and p.name != 'B.Weeden' and p.name != 'J.Prosch' and p.name != 'B.Daniels' and p.name != 'T.Yates':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Houston's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## Tennessee Titans

games = nflgame.games(2015, week=range(1,curr), away = "TEN", home ="TEN")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'M.Mariota' and p.name != 'Z.Mettenberger' and p.name != 'A.Tanney' and p.name != 'A.Andrews':

 #       print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Tennessee's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'A.Andrews' and p.name != 'D.McCluster' and p.name != 'D.Cobb' and p.name != 'B.Sankey' and p.name != 'M.Mariota' and p.name != 'Z.Mettenberger' and p.name != 'J.Fowler' and p.name != 'K.Wright' and p.name != 'D.Walker' and p.name != 'T.McBride' and p.name != 'H.Douglas':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Tennessee's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## Jacksonville Jaguars

games = nflgame.games(2015, week=range(1,curr), away = "JAC", home ="JAC")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'B.Bortles' and p.name != 'B.Walters':

 #       print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Jacksonville's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'T.Yeldon' and p.name != 'D.Robinson' and p.name != 'B.Bortles' and p.name != 'T.Gerhart' and p.name != 'J.Gray' and p.name != 'B.Pierce' and p.name != 'C.Grant' and p.name != 'M.lee' and p.name != 'T.Washington' and p.name != 'T.Alualu':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Jacksonville's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score


## Pittsburgh Steelers

games = nflgame.games(2015, week=range(1,curr), away = "PIT", home ="PIT")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'B.Roethlisberger' and p.name != 'M.Vick' and p.name != 'L.Jones':

 #       print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Pittsburgh's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'De.Williams' and p.name != 'L.Bell' and p.name != 'M.Vick' and p.name != 'F.Toussaint' and p.name != 'B.Roethlisberger' and p.name != 'M.Bryant' and p.name != 'L.Jones' and p.name != 'J.Todman' and p.name != 'W.Johnson' and p.name != 'A.Brown' and p.name != 'H.Miller':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Pittsburgh's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score




## Baltimore Ravens

games = nflgame.games(2015, week=range(1,curr), away = "BAL", home ="BAL")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'J.Flacco' and p.name != 'R.Mallett' and p.name != 'J.Clausen' and p.name != 'M.Schaub' and p.name != 'S.Koch':

#        print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Baltimore's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'J.Forsett' and p.name != 'J.Allen' and p.name != 'T.West' and p.name != 'L.Taliaferro' and p.name != 'J.Flacco' and p.name != 'J.Clausen' and p.name != 'M.Schaub' and p.name != 'C.Givens' and p.name != 'M.Campanaro' and p.name != 'T.Magee' and p.name != 'K.Juszczyk' and p.name != 'S.Koch' and p.name != 'R.Mallett' and p.name != 'A.Levine':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Baltimore's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score


## Cincinnati Bengals

games = nflgame.games(2015, week=range(1,curr), away = "CIN", home ="CIN")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'A.Dalton' and p.name != 'A.McCarron':

#        print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Cincinnati's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'J.Hill' and p.name != 'G.Bernard' and p.name != 'A.Dalton' and p.name != 'A.McCarron' and p.name != 'M.Sanu' and p.name != 'M.Jones' and p.name != 'R.Burkhead':

    #    print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Cincinnati's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score




## Cleveland Browns

games = nflgame.games(2015, week=range(1,curr), away = "CLE", home ="CLE")

# Combine stats for the players that are a part of games
players = nflgame.combine_game_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

    if p.name != 'J.McCown' and p.name != 'J.Manziel' and p.name != 'A.Davis':

#        print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds


defense = "There were %d passing yards allowed for Cleveland's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

    if p.name != 'I.Crowell' and p.name != 'D.Johnson' and p.name != 'J.Manziel' and p.name != 'R.Turbin' and p.name != 'J.McCown' and p.name != 'A.Davis' and p.name != 'T.Benjamin' and p.name != 'J.Poyer' and p.name != 'T.Pryor' and p.name != 'G.Winston':

   #     print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for Cleveland's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score



## The Chargers: Destination Unknown

games = nflgame.games(2015, week=range(1,curr), away = "SD", home ="SD")

# Combine stats for the players that are a part of games
players = nflgame.combine_max_stats(games)


# Sort and print the stats based on constraints
passed = 0;
touch  = 0;
for p in players.passing().sort('passing_yds').limit(40):

  #  if p.name != 'J.McCown' and p.name != 'J.Manziel' and p.name != 'A.Davis':
    if p.team != 'SD':
#        print p, p.passing_att, p.passing_yds, p.passing_tds    
    
        passed = passed + p.passing_yds
	touch  = touch  + p.passing_tds

defense = "There were %d passing yards allowed for Charger's Defense"
print defense % (passed)
pass_per_game = passed/640
touch_per_game = (touch*3)/32
score = pass_per_game + touch_per_game
print score
touch = 0;
rushed = 0;
score = 0;
for p in players.rushing().sort('rushing_yds').limit(50):

 #   if p.name != 'I.Crowell' and p.name != 'D.Johnson' and p.name != 'J.Manziel' and p.name != 'R.Turbin' and p.name != 'J.McCown' and p.name != 'A.Davis' and p.name != 'T.Benjamin' and p.name != 'J.Poyer' and p.name != 'T.Pryor' and p.name != 'G.Winston':
    if p.team != 'SD':
        print p, p.rushing_att, p.rushing_yds, p.rushing_tds    

        rushed = rushed + p.rushing_yds
	touch  = touch  + p.rushing_tds


defense = "There were %d rushing yards allowed for the Charger's Defense"
print defense % (rushed)
rush_per_game = rushed/640
touch_per_game = (touch*3)/16
score = pass_per_game + touch_per_game
print score


