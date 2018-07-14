import pymysql
from random import randint

db = pymysql.connect("localhost", "root", "city2939", "football_sim")
c = db.cursor()

def goals():
    return randint(0, 6)

def assists(goalnumber):
    return randint(0,goalnumber+1)

def season_stats(query):
    rows = c.fetchall()
    for row in rows:
        print(row[1], "-", row[2], "-", row[6], "-", row[7], "-", row[8])

def game_stats(query):
    rows = c.fetchall()
    for row in rows:
        print(row[0], "-", row[1], "-", row[2])

def game():
    print("")
    games_total = 0
    while games_total <= 38:
        next_game = str(input("Start the next game by pressing Enter, or press 1 to see the current Season Stats: "))
        print("")
        if next_game == "":
            game_goals = goals()
            game_assists = assists(game_goals)

            # getting goals for game and assists for games - need to attribute these to random players in game_goals and game_assists (Use ID?)
            #exclude attributing to goalkeepers
            #commit these goals & assists to mancity table (this is a running talley), before setting game_goals and game_assists back to 0


            game_stats(f"select * from game_goals")
            game_stats(f"select * from game_assists")
            query = f"delete from game_goals where gamegoals>0"
            c.execute(query)
            query_one = f"delete from game_assists where gameassists>0"
            c.execute(query_one)
            db.commit()
            games_total += 1


        if next_game == 1:
            print("")
            season_stats(f"select * from mancity")
            print("")

    print ("The Season is over! Here are the final stats for your team: ")
    print("")
    season_stats(f"select * from mancity")
    print("")


        # number of games = GK can play 38, Starters 28, Subs 7, Reserves 3




