import mysql.connector

# Create Connection Obj
import UserRequest

db = mysql.connector.connect(
    host=UserRequest.host,
    user=UserRequest.user,
    password=UserRequest.pw,
)

cursor = db.cursor()

queryGames = "SHOW DATABASE"
queryMods = "SELECT mod_name, mod_version, mod_url FROM %s"
