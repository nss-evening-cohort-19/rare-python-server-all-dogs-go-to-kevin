import sqlite3
import json
from models.reaction import Reaction

def get_all_reactions():
    with sqlite3.connect("./db.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            r.id,
            r.label,
            r.image_url
        FROM Reactions r
        """)
        
        reactions = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
          
            reaction = Reaction(row['id'], row['label'], row['image_url'])
            
            reactions.append(reaction.__dict__)

        return json.dumps(reactions)

def get_single_reaction(id):
  with sqlite3.connect("./db.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        r.id,
        r.label,
        r.image_url
    FROM Reactions r
    WHERE r.id = ?
    """, ( id, ))
    
    data = db_cursor.fetchone()
    
    reaction = Reaction(data['id'], data['label'], data['image_url'])
    
    return json.dumps(reaction.__dict__)
  
def create_reaction(new_reaction):
  
  with sqlite3.connect("./db.sqlite3") as conn:
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    INSERT INTO Reactions
        ( id, label, image_url )
    VALUES ( ?, ?, ? );
    """, (new_reaction['id'], new_reaction['label'], new_reaction['image_url'] ))
    
    id = db_cursor.lastrowid
    
    new_reaction['id'] = id
    
  return json.dumps(new_reaction)

def delete_reaction(id):
  
  with sqlite3.connect("./db.sqlite3") as conn:
      db_cursor = conn.cursor()
      
      db_cursor.execute("""
      DELETE FROM REACTIONS
      WHERE id = ?
      """, ( id, ))
      
def update_reaction(id, new_reaction):
  
  with sqlite3.connect("./db.sqlite3") as conn:
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    UPDATE Reactions
    SET
        id = ?,
        label = ?,
        image_url = ?
    WHERE id = ?
    """, (new_reaction['id'], new_reaction['label'], new_reaction['image_url'], id, ))
  rows_affected = db_cursor.rowcount
  
  if rows_affected == 0:
      return False
  else:
      return True
    
# def get_reactions_by_post(post_id):
  
#     with sqlite3.connect("./db.sqlite3") as conn:
#       conn.row_factory = sqlite3.Row
#       db_cursor = conn.cursor()
      
#       db_cursor.execute("""
#       SELECT * FROM Reactions r
#       JOIN Posts p on r.
#                         """,)
