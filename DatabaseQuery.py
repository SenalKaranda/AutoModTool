import DatabaseAccess.Access
from DatabaseAccess import *

DbA = DatabaseAccess
db = DbA.Access.db
cursor = DbA.Access.cursor

gameIDArray = []

cursor.execute(DbA.Access.queryGames)

for x in cursor:
    gameIDArray[x] = cursor[x]

# cursor.execute(DbA.Access.queryMods, DbA.Access.UserRequest.gameID)
# for (mod_name, mod_version, mod_url) in cursor:
#     print("{} | {} | {}".format(mod_name, mod_version, mod_url))

cursor.close()
db.close()
