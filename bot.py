from discord import Client
from datetime import datetime
from time import sleep
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
    dmIDs = list(map(int, config[1:]))


@client.event
async def on_ready():
    print("We do a bit of trolling. (The script is connected to the client and is active)")
    print(f"Logged in as {client.user.name}")
    while 1:
        if not (datetime.now().time().strftime("%H:%M") in ["07:27", "19:27"]):
            wysiSent = False
            sleep(50)
        elif not wysiSent:
            print("+=============================================================================================+")
            print("| It is the current local time of the funny WYSI cookiezi funny blue zenith 727 funny number! |")
            print("|" + " "*((52 - len(configFn)) // 2) + f"Sending messages to user IDs listed in {configFn}..." + " "*((51 - len(configFn)) // 2) + "|")
            print("+=============================================================================================+")
            for dm in dmIDs:
                await (await client.fetch_user(dm)).send("WYSI\nWYFSI")
                await (await client.fetch_user(dm)).send("https://tenor.com/view/wysi-gif-21694798")
            wysiSent = True


client.run(clientToken, bot=False)
