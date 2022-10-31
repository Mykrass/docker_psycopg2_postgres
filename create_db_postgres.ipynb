import psycopg2

conn = psycopg2.connect(
    dbname="postgres", user="postgres", password="postgres", host="192.168.32.3"
)

conn.autocommit = True
cur = conn.cursor()

DATA_PROD_USER_PWD = "changeme"
DATA_VIEW_USER_PWD = "changeme"

# create user and detach password from command
# also add an IF NOT EXIST clause as a hack from
# https://stackoverflow.com/questions/8092086/create-postgresql-role-user-if-it-doesnt-exist
cur.execute(f"""
CREATE USER data_prod_user WITH PASSWORD '{DATA_PROD_USER_PWD}';
CREATE GROUP readonly WITH NOLOGIN;
CREATE USER analyst1 WITH PASSWORD '{DATA_VIEW_USER_PWD}' IN GROUP readonly;
""")

# create db
print("CREATE DATABASE ihw OWNER postgres")
cur.execute("CREATE DATABASE ihw OWNER postgres")

conn.commit()
conn.close()
