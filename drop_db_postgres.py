# revoke all permissions by default. 
# Use this to start all over.
import psycopg2

conn = psycopg2.connect(
    dbname="postgres", user="postgres", password="postgres", host="192.168.32.3"
)

conn.autocommit = True
cur = conn.cursor()

# drop users
cur.execute("""
DROP USER data_prod_user;
DROP USER analyst1;
DROP GROUP readonly;
""")

# drop db
print("DROP DATABASE IF EXISTS ihw")
cur.execute("DROP DATABASE IF EXISTS ihw")

conn.commit()
conn.close()
