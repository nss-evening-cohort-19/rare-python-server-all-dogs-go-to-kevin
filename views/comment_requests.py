import sqlite3
import json
from models import Comment

COMMENTS = [
    {
      "id": 1,
      "post_id": 2,
      "author_id": 3,
      "content" : "A Comment"
    },
    {
      "id": 2,
      "post_id": 3,
      "author_id": 4,
      "content" : "Another Comment"
    }
]

def update_comment(id, new_comment):
    with sqlite3.connect("./kennel.sqlite3") as conn:
      db_cursor = conn.cursor()
      
      db_cursor.execute("""
      UPDATE Comment
          SET
              post_id = ?,
              author_id = ?,
              content = ?
      WHERE id = ?
      """, (new_comment['id'], new_comment['post_id'], new_comment['author_id'], new_comment['content'], id, ))
      
      rows_affected = db.cusrsor.rowcount
      
      if rows_affected == 0:
        
        return False
      
      else:
        
        return True
