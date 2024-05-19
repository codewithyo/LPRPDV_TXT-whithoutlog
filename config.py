import os

API_ID = API_ID = 23634056

API_HASH = os.environ.get("API_HASH", "f2debf49c2f57bad88086ecd17cb5df3")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7174606656:AAES4xrsYwn9gi8O9knJBM0wwC2NihyGKTw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5082207960))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5082207960").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


