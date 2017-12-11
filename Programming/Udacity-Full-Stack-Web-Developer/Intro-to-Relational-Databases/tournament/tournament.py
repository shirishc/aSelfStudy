#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    DBConn = connect()
    cur = DBConn.cursor()
    cur.execute("delete from matches")
    DBConn.commit()
    DBConn.close()
    
def deletePlayers():
    """Remove all the player records from the database."""
    DBConn = connect()
    cur = DBConn.cursor()
    cur.execute("delete from matches")
    cur.execute("delete from players")
    DBConn.commit()
    DBConn.close()
    

def countPlayers():
    """Returns the number of players currently registered."""
    DBConn = connect()
    cur = DBConn.cursor()
    cur.execute("select count(*) from players")
    rows = cur.fetchall()
    DBConn.close()
    return rows[0][0]
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DBConn = connect()
    cur = DBConn.cursor()
    cur.execute("insert into players(name) values(%s)", (name,))
    DBConn.commit()
    DBConn.close()
    

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DBConn = connect()
    cur = DBConn.cursor()
    cur.execute("select * from STANDINGS order by wins desc")
    standings = [(row[0], row[1], row[2], row[3])
                    for row in cur.fetchall()]
    DBConn.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DBConn = connect()
    cur = DBConn.cursor()
    cur.execute("insert into matches(winner, loser) values(%s, %s)", (winner, loser))
    DBConn.commit()
    DBConn.close()
    
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    swissPairs = []
    idx = 0
    while (idx <= len(standings)-2):
        print(idx)
        swissPairs.append((standings[idx][0], standings[idx][1], 
                        standings[idx+1][0], standings[idx+1][1]))
        idx = idx + 2
    return swissPairs