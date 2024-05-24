import os
from os import getenv


API_ID = int(getenv("API_ID", "24074986"))
API_HASH = getenv("API_HASH", "f4f6272a85d0e50e39a24cb378be118d")
BOT_USERNAME = getenv("BOT_USERNAME", "TESTBETAHEXAROBOT")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "7038466993:AAF5TX7gwoIpidTfWEqr7w2HEH1okTwP8Es")
OWNER_ID = int(getenv("OWNER_ID", "6534367642"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6758236533").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://tiwarireeta004:peqxLEd36RAg7ors@cluster0.furypd3.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQFvWuoAvD86o7jmcZALt6w5yStPJQG__49gukwHx2vkH0wM6d6_EmwPxfiHxnLVbnWCxd92w6UgT5l4VyLx_2Y5_fd-AW57gT1eKfgT9d8VRwGJ60z4EhnNKk6cI2KUxZsCXfwIXwuvzIjvbt3H8vFSg_Y1iOo4ll-ln5Yt2e8yB_daxmLw8Frys1Jg-aM2kWOcb3uQJTum29iRDjx8nkwKXVqYHPhCCMax4s3KCNE_edx1w2xtuHdIOZQT-wun-W0ABps48CCsPVpyd5VrZyYe2O_fpBpfMpfxjiGEBehgDDIFWPHCdqfFa6yL3yd3liM4HqhuMcY5d70qRDlgTc_ps0JeWwAAAAGFeomaAA")
