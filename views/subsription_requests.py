import sqlite3
import json
from models import Subscription

def get_all_subs():
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on
        FROM Subscriptions s
        """)

        subs = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            sub = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_on'])

            subs.append(sub.__dict__)

        return json.dumps(subs)

def get_single_sub(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on
        FROM Subscriptions s
        WHERE s.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        sub = Subscription(data['id'], data['follower_id'], data['author_id'], data['created_on'])

        return json.dumps(sub.__dict__)

def create_sub(new_sub):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Subscriptions
            ( follower_id, author_id, created_on )
        VALUES
            ( ?, ?, ? );
        """, (new_sub['follower_id'], new_sub['author_id'],
            new_sub['created_on'] ))

        id = db_cursor.lastrowid

        new_sub['id'] = id

    return json.dumps(new_sub)

def delete_sub(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Subscriptions
        WHERE id = ?
        """, ( id, ))

def update_sub(id, new_sub):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Subscriptions
            SET
                follower_id = ?,
                author_id = ?,
                created_on = ?
        WHERE id = ?
        """, (new_sub['follower_id'], new_sub['author_id'],
            new_sub['created_on'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
