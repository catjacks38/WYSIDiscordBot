from discord import Client
from datetime import datetime
import sys

client = Client()
wysiSent = False

try:
    configFn = sys.argv[1]
except:
    print("ERROR! Missing config file path!")
    exit(-1)

with open(configFn, "rt") as configFile:
    config = configFile.readlines()
    clientToken = config[0]
    dmIDs = map(int, config[1:])


@client.event
async def on_ready():
    print("We do a bit of trolling. (The script is connected to the client and is active)")
    print(f"Logged in as {client.user.name}")
    while 1:
        if not (datetime.now().time().strftime("%H:%M") in ["07:27", "19:27"]):
            wysiSent = False
        elif not wysiSent:
            print("+=============================================================================================+")
            print("| It is the current local time of the funny WYSI cookiezi funny blue zenith 727 funny number! |")
            print(f"|                    Sending messages to user IDs listed in {configFn}...                     |")
            print("+=============================================================================================+")
            for dm in dmIDs:
                await (await client.fetch_user(dm)).send("WYSI")
                await (await client.fetch_user(dm)).send("WYFSI")
                await (await client.fetch_user(dm)).send("https://tenor.com/view/wysi-gif-21694798")
            wysiSent = True


client.run(clientToken, bot=False)
