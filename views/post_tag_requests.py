import sqlite3
import json
from models import (
    Post_Tag,
    Tag,
)

def get_all_post_tags():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id,
            t.id,
            t.label
        FROM PostTags pt
        JOIN tags t
            on t.id = pt.tag_id
        """)

        post_tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = Post_Tag(row['id'], row['post_id'], row['tag_id'])

            tag = Tag(row['id'], row['label'])

            post_tag.tag = tag.__dict__
            post_tags.append(post_tag.__dict__)
    return json.dumps(post_tags)

def create_post_tag(new_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO PostTags
                ( post_id, tag_id )
                VALUES
                ( ?, ? )
                """, (new_tag['post_id'], new_tag['tag_id'] ))

        id = db_cursor.lastrowid

        new_tag['id'] = id

    return json.dumps(new_tag)

def remove_post_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM PostTags
        WHERE id = ?
        """, ( id, ))

