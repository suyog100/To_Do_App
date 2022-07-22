import sqlite3

# establishing a connection with our database
conn = sqlite3.connect("users.db")

# creating a curson
c = conn.cursor()

# creating a table for our users database
# c.execute(""" CREATE TABLE users(
#         firstName text,
#         lastName text,
#         email text,
#         password text
#     )""")


# committing the changes
conn.commit()

# closing the connection

