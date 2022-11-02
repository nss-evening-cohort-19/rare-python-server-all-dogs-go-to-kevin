import sqlite3
import json
from models import Comment

<<<<<<< HEAD
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
=======
def get_all_comments():
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content
        FROM Comments c
        """)

        comments = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])

            comments.append(comment.__dict__)

        return json.dumps(comments)

def get_single_comment(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content
        FROM Comments c
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        comment = Comment(data['id'], data['post_id'], data['author_id'], data['content'])

        return json.dumps(comment.__dict__)
>>>>>>> 2fb1433ed887ba12640a0b2c8f96901f7db281fc
