import os
from os import getenv


API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_USERNAME = getenv("BOT_USERNAME", "YumikooBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6743158347:AAG0lotMQpA7jGYaFmQN5DtIuNoJDxzA-yo")
OWNER_ID = int(getenv("OWNER_ID", "6691393517"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6691393517").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQFYNvIAZ1yg6dKk5_rSeO3UAhVcMPij6AFkjVRk-4-lqeIzcHoO7QlXMBbBDtu-8ydfKJGTGQpgy3BbClq7-T_rRZbUJfPULWUpLuTdF4ljlvIWKHMw6VyVEuzRf_6JJGVEyN0fAMIrSmdwiKuZ1zUx9HpVqPw6")
