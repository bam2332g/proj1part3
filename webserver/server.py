#!/usr/bin/env python2.7

"""
Columbia W4111 Intro to databases
Example webserver

To run locally

    python server.py

Go to http://localhost:8111 in your browser


A debugger such as "pdb" may be helpful for debugging.
Read about it online.

bam2189 2015
"""

import os
from decimal import Decimal
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


#
# The following uses the sqlite3 database test.db -- you can use this for debugging purposes
# However for the project you will need to connect to your Part 2 database in order to use the
# data
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@w4111db1.cloudapp.net:5432/proj1part2
#
# For example, if you had username ewu2493, password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://ewu2493:foobar@w4111db1.cloudapp.net:5432/proj1part2"
#
#DATABASEURI = "sqlite:///test.db"
DATABASEURI = "postgresql://rk2658:879@w4111db1.cloudapp.net:5432/proj1part2"

#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)

#
# START SQLITE SETUP CODE
#
# after these statements run, you should see a file test.db in your webserver/ directory
# this is a sqlite database that you can query like psql typing in the shell command line:
# 
#     sqlite3 test.db
#
# The following sqlite3 commands may be useful:
# 
#     .tables               -- will list the tables in the database
#     .schema <tablename>   -- print CREATE TABLE statement for table
# 
# The setup code should be deleted once you switch to using the Part 2 postgresql database
#


###engine.execute("""DROP TABLE IF EXISTS test;""")
###engine.execute("""CREATE TABLE IF NOT EXISTS test (
###  id serial,
###  name text
###);""")
###engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")


#
# END SQLITE SETUP CODE
#



@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request

  The variable g is globally accessible
  """
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't the database could run out of memory!
  """
try:
    g.conn.close()
except Exception as e:
    pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a POST or GET request
#
# If you wanted the user to go to e.g., localhost:8111/foobar/ with POST or GET then you could use
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important) # 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
# 
@app.route('/', methods=["POST", "GET"])
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """
  # DEBUG: this is debugging code to see what request looks like
  #print request.args


  #
  # example of a database query
  #
  cursor = g.conn.execute("SELECT *  FROM sportsleague")
  names = []
  for result in cursor:
    names.append(result['leagueid'])  # can also be accessed using result[0]
  cursor.close()

  #
  # Flask uses Jinja templates, which is an extension to HTML where you can
  # pass data to a template and dynamically generate HTML based on the data
  # (you can think of it as simple PHP)
  # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
  #
  # You can see an example template in templates/index.html
  #
  # context are the variables that are passed to the template.
  # for example, "data" key in the context variable defined below will be 
  # accessible as a variable in index.html:
  #
  #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
  #     <div>{{data}}</div>
  #     
  #     # creates a <div> tag for each element in data
  #     # will print: 
  #     #
  #     #   <div>grace hopper</div>
  #     #   <div>alan turing</div>
  #     #   <div>ada lovelace</div>
  #     #
  #     {% for n in data %}
  #     <div>{{n}}</div>
  #     {% endfor %}
  #
  context = dict( data = names )


  #
  # render_template looks in the templates/ folder for files.
  # for example, the below file reads template/index.html
  #
  return render_template("home.html", **context)

#
# This is an example of a different path.  You can see it at
# 
#     localhost:8111/another/
#
# notice that the function name is another() rather than index()
# the functions for each app.route needs to have different names
#
@app.route('/nba.html', methods=["POST", "GET"])
def nba():
  cursor = g.conn.execute("SELECT *  FROM sportsleague WHERE name='NBA'")
  leagueInfo = []
  for result in cursor:
    leagueInfo.append(result['leagueid'])# can also be accessed using result[0]
    leagueInfo.append(result['avgyrsofexp'])
    leagueInfo.append(result['numofplyronteam'])
    leagueInfo.append(result['avgageofplyr'])
    leagueInfo.append(result['avgageofteam'])
    leagueInfo.append(result['avgwinpct'])
  cursor.close()

  context = dict(data = leagueInfo)
  return render_template("nba.html", **context)

@app.route('/nba-player.html', methods=["POST", "GET"])
def nbaPlayer():
  cursor = g.conn.execute("SELECT *  FROM player WHERE leagueid=1")
  #cursor = g.conn.execute("SELECT *  FROM sportsleague2")
  nbaPlayers = []
  for result in cursor:
      nbaPlayers.append(result['name'])
  cursor.close()

  context = dict(data = nbaPlayers)
  return render_template("nba-player.html", **context)

@app.route('/nbaPSearch', methods=["POST"])
def nbaPSearch():
  pName = request.form['pName']
  q = "SELECT playerid FROM player WHERE name = %s "
  #print(pName)
  #print q
  pid = [] 
  
  cursor = g.conn.execute(q, (pName,))
  for result in cursor:
      pid.append(result[0])
  cursor.close()

  pid2 = pid[0]
  #print(pid2)
  q2 = "SELECT * FROM nbaplayerstats WHERE playerid = %s ORDER BY year"
  #print q2
  cursor = g.conn.execute(q2, (pid2,))
  playerStats = []
  for result in cursor:
      #print(result['year'])
      #playerStats.append(pName)
      ga = Decimal(result['games'])
      playerStats.append(result['year'])
      #playerStats.append((result['games'])/)
      playerStats.append(format(Decimal(result['turnovers'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['steals'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['blks'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['pts'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['fgm'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['fga'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['tpm'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['tpa'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['ftm'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['fta'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['rebs'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['assists'])/ga, '.2f'))
      playerStats.append(result['allstar'])
      playerStats.append(result['mvp'])
  cursor.close()

  q3 = "SELECT name FROM topplayer t1 WHERE t1.topplayerid = (SELECT topplayerid FROM predictions t2 WHERE t2.playerid= %s)"
  cursor = g.conn.execute(q3, (pid2,))
  playerPredictions = []
  for result in cursor:
    #print(result[0])
    playerPredictions.append(result[0])
  cursor.close()
  
  q4 = "SELECT * FROM predictions  WHERE playerid= %s"

  cursor = g.conn.execute(q4, (pid2,))
  for result in cursor:
      playerPredictions.append(result['similarityscore'])
      playerPredictions.append(result['probofallstar'])
      playerPredictions.append(result['probofmvp'])
  cursor.close()

  context = dict(data = playerStats, player=pName, preds=playerPredictions)
  return render_template("nba-player-stats.html", **context)

@app.route('/nba-team.html', methods=["POST", "GET"])
def nbaTeam():
  cursor = g.conn.execute("SELECT *  FROM team WHERE leagueid=1")
  nbaTeams = []
  for result in cursor:
      nbaTeams.append(result['name'])
  cursor.close()

  context = dict(data = nbaTeams)
  return render_template("nba-team.html", **context)

@app.route('/nbaTSearch', methods=["POST"])
def nbaTSearch():
  tName = request.form['tName']
  q = "SELECT teamid FROM team WHERE name = %s"
  print(tName)
  print q
  tid = [] 
  
  cursor = g.conn.execute(q, (tName,))
  for result in cursor:
      tid.append(result[0])
  cursor.close()

  tid2 = tid[0]
  #print(tid2)
  q2 = "SELECT * FROM player WHERE  teamid = %s AND leagueid = 1"
  #print q2
  cursor = g.conn.execute(q2, (tid2,))
  teamRoster = []
  for result in cursor:
      #print(result['year'])
      teamRoster.append(result['name'])
      teamRoster.append(result['position'])
  cursor.close()

  q3="SELECT * FROM team WHERE teamid = %s AND leagueid=1"
  cursor=g.conn.execute(q3, (tid2,))
  predictions= []
  for result in cursor:
      predictions.append(result['wins'])
      predictions.append(result['losses'])
      predictions.append(result['ties'])
      predictions.append(result['numberofchampionships'])
      predictions.append(result['probofwinningchmp'])
  cursor.close()

  context = dict(data = teamRoster, team=tName, preds=predictions)
  return render_template("nba-team-rosters.html", **context)


@app.route('/nfl.html', methods=["POST", "GET"])
def nfl():
  cursor = g.conn.execute("SELECT *  FROM sportsleague WHERE name='NFL'")
  leagueInfo = []
  for result in cursor:
    leagueInfo.append(result['leagueid'])# can also be accessed using result[0]
    leagueInfo.append(result['avgyrsofexp'])
    leagueInfo.append(result['numofplyronteam'])
    leagueInfo.append(result['avgageofplyr'])
    leagueInfo.append(result['avgageofteam'])
    leagueInfo.append(result['avgwinpct'])
  cursor.close()

  context = dict(data = leagueInfo)
  return render_template("nfl.html", **context)

@app.route('/nfl-player.html', methods=["POST", "GET"])
def nflPlayer():
  cursor = g.conn.execute("SELECT *  FROM player WHERE leagueid=0")
  #cursor = g.conn.execute("SELECT *  FROM sportsleague2")
  nflPlayers = []
  for result in cursor:
      nflPlayers.append(result['name'])
  cursor.close()

  context = dict(data = nflPlayers)
  return render_template("nfl-player.html", **context)

@app.route('/nflPSearch', methods=["POST"])
def nflPSearch():
  pName = request.form['pName']
  #q = "SELECT playerid FROM player WHERE name = %s "
  q = "SELECT * FROM player WHERE name = %s "
  #print(pName)
  #print q
  pid = [] 
  position = ''
  cursor = g.conn.execute(q, (pName,))
  for result in cursor:
      pid.append(result['playerid'])
      position = result['position']
  cursor.close()

  pid2 = pid[0]
  #print(pid2)
  q2 = "SELECT * FROM nflplayerstats WHERE playerid = %s ORDER BY year"
  #print q2
  cursor = g.conn.execute(q2, (pid2,))
  playerStats = []
  for result in cursor:
      #print(result['year'])
      #playerStats.append(pName)
      ga = Decimal(result['games'])
      
      playerStats.append(result['year'])
      #playerStats.append((result['games']))
      playerStats.append(format(Decimal(result['qbyards'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['qbinter'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['qbsacks'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['qbcompl'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['qbatt'])/ga, '.2f'))
      playerStats.append(result['qbrating'])
      playerStats.append(format(Decimal(result['rushingatt'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['rushingyds'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['receptions'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['receivingyds'])/ga, '.2f'))
      playerStats.append(format(Decimal(result['td'])/ga, '.2f'))
      playerStats.append(result['probowl'])
      playerStats.append(result['mvp'])
  cursor.close()

  q3 = "SELECT name FROM topplayer t1 WHERE t1.topplayerid = (SELECT topplayerid FROM predictions t2 WHERE t2.playerid= %s)"
  cursor = g.conn.execute(q3, (pid2,))
  playerPredictions = []
  for result in cursor:
    #print(result[0])
    playerPredictions.append(result[0])
  cursor.close()
  
  q4 = "SELECT * FROM predictions  WHERE playerid= %s"

  cursor = g.conn.execute(q4, (pid2,))
  for result in cursor:
      playerPredictions.append(result['similarityscore'])
      playerPredictions.append(result['probofallstar'])
      playerPredictions.append(result['probofmvp'])
  cursor.close()

  context = dict(data = playerStats, player=pName, preds=playerPredictions)
  return render_template("nfl-player-stats.html", **context)

@app.route('/nfl-team.html', methods=["POST", "GET"])
def nflTeam():
  cursor = g.conn.execute("SELECT *  FROM team WHERE leagueid=0")
  nflTeams = []
  for result in cursor:
      nflTeams.append(result['name'])
  cursor.close()

  context = dict(data = nflTeams)
  return render_template("nfl-team.html", **context)


@app.route('/nflTSearch', methods=["POST"])
def nflTSearch():
  tName = request.form['tName']
  q = "SELECT teamid FROM team WHERE name = %s"
  #print(tName)
  #print q
  tid = [] 
  
  cursor = g.conn.execute(q, (tName,))
  for result in cursor:
      tid.append(result[0])
  cursor.close()

  tid2 = tid[0]
  #print(tid2)
  q2 = "SELECT * FROM player WHERE  teamid = %s AND leagueid = 0"
  #print q2
  cursor = g.conn.execute(q2, (tid2,))
  teamRoster = []
  for result in cursor:
      #print(result['year'])
      teamRoster.append(result['name'])
      teamRoster.append(result['position'])
  cursor.close()

  q3="SELECT * FROM team WHERE teamid = %s AND leagueid=0"
  cursor=g.conn.execute(q3, (tid2,))
  predictions= []
  for result in cursor:
      predictions.append(result['wins'])
      predictions.append(result['losses'])
      predictions.append(result['ties'])
      predictions.append(result['numberofchampionships'])
      predictions.append(result['probofwinningchmp'])
  cursor.close()

  context = dict(data = teamRoster, team=tName, preds=predictions)
  return render_template("nfl-team-rosters.html", **context)

if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using

        python server.py

    Show the help text using

        python server.py --help

    """

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
