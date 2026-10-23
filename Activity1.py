import sqlite3 
import pandas as pd

# - - -  PARR !: Build and Explore the Tr=ables - - - -

conn = sqlite3.connect(':memory:')

conn.execute("CREATE TABLE recipe (recipe_id INTEGER PRIMARY KEY, recipe_name TEXT NOT NULL, cuisine TEXT NOT NULL, prep_mins INTEGER NOT NULL)")

conn.execute("CREATE TABLE ingredient (ingredient_id INTEGER PRIMARY KEY, recipe_id INTEGER NOT NULL, item TEXT NOT NULL, quantity_g INTEGER NOT NULL)")

conn.executemany("INSERT INTO recipe VALUES (?, ?, ?, ?,)",[
    (1, 'Pasta', 'Italian',  20),
    (2, 'Tacos', 'Mexican',  15),
    (3, 'sushi', 'Japanese', 45),
    (4, 'Pizza', 'Italian',  30),
    (5, 'Salad', 'Greek',    10),
])

conn.executemany("INSERT INTO ingredient VALUES (?, ?, ?, ?)",[
    (1, 1, 'Pasta',       200),
    (2, 1, 'Sauce',       150),
    (3, 2, 'Tortilla',     80),
    (4, 2, 'Beef',        120),
    (5, 3, 'Salmon',      180),
    (6, 4, 'Dough',       250),
    (7, 5, 'Lettuce',     50),
    (8, 5, 'Feta',        40),
])

conn.commit()

print("Recipe table:")
print(pd.read_sql("SELECT * FROM recipe", conn))
print()
print("Ingridient table:")
print(pd.read_sql("SELECT * FROM ingridient", conn))
print()

# - - - - PART 2: Alias for Colums - - - -
 
