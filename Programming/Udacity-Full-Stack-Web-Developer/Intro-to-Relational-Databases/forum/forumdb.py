#
# Database access functions for the web forum.
# 

import time
import psycopg2
import bleach

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DBConn = psycopg2.connect("dbname=forum")
    cur = DBConn.cursor()
    cur.execute("""select * from posts order by time desc""")
    posts = [{'content': str(row[0]), 'time': str(row[1]), 'id': (row[2])} 
              for row in cur.fetchall()]
    # Sorting now happening in the database
    # posts.sort(key=lambda row: row['time'], reverse=True)
    DBConn.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    # t = time.strftime('%c', time.localtime())
    
    DBConn = psycopg2.connect("dbname=forum")
    cur = DBConn.cursor()
    content = bleach.clean(content)
    # content = bleach.linkify(content)
    cur.execute("insert into posts(content) values(%s)",  (content,))
    DBConn.commit()
    DBConn.close()
    
