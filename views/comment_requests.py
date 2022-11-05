import sqlite3
import json
from models import Comment
from models.post import Post

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
        # JOIN Post p
        #   ON p.id = c.post_id
        """)

        comments = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])
            
            # post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
            
            # comment.post = post.__dict__

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

def delete_comment(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, ( id, ))

def update_comment(id, new_comment):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Comments
        SET
            post_id = ?,
            author_id = ?,
            content = ?
        WHERE id = ?
        """, (new_comment['post_id'], new_comment['author_id'], new_comment['content'], id, ))
    rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def get_comments_by_post(post):
  
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        select
            c.id,
            c.post_id,
            c.author_id,
            c.content
        from Comments c
        WHERE c.post_id = ?
        """, ( post, ))
        
        comments = []
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])
            comments.append(comment.__dict__)
            
    return json.dumps(comments)
