from discord import Client
from datetime import datetime
import sys

client = Client()
WysiSent = False

try:
    configFn = sys.argv[1]
except:
    print("ERROR! Missing config file path!")
    exit(-1)

with open(configFn, "r") as configFile:
    config = configFile.read().split("\n")
    clientToken = config[0]
    dmIDs = map(int, config[1:])


@client.event
async def on_ready():
    print("We do a bit of trolling. (The script is connected to the client and is active)")
    print(f"Logged in as {client.user.name}")
    while 1:
        if (datetime.now().hour == 19 or datetime.now().hour == 7) and datetime.now().minute == 27 and not WysiSent:
            for dm in dmIDs:
                print("+=============================================================================================+")
                print("| It is the current local time of the funny WYSI cookiezi funny blue zenith 727 funny number! |")
                print(f"|                    Sending messages to user IDs listed in {configFn}...                     |")
                print("+=============================================================================================+")
                await (await client.fetch_user(dm)).send("WYSI")
                await (await client.fetch_user(dm)).send("WYFSI")
                await (await client.fetch_user(dm)).send("https://tenor.com/view/wysi-gif-21694798")
            WysiSent = True
        else:
            WysiSent = False


client.run(clientToken, bot=False)
