import os
from os import getenv


API_ID = int(getenv("API_ID", "27205215"))
API_HASH = getenv("API_HASH", "105e1f779e13d401ff0131bc88ed5063")
BOT_USERNAME = getenv("BOT_USERNAME", "Dazai_ixbot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6964505365:AAFzNSGY1ReQ2B68zjLzb3AAZAneVm7Epok")
OWNER_ID = int(getenv("OWNER_ID", "5054912509"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6758236533").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQCVPypGMadCL97iCWzxOa2PqkVF2kURgZ-XDdCfwKaU2zGK945kaf6_7DzeX8ZKmrbPSgLBZ1pGqTy_TcwamRHZD475CSE8EdoO9pcoWZXM4kIgVJVYU9j_Nb4ijFof2fHAeF71MxQtRroSVqj_fQWemuu1sP_nzo-NCUjGiyiF-I_ceDgNNjLsmQEgH8sKa2XQoWlxGFLb2UkkhYOk3jpOn6EzSq3bGVje3iKjSwhhpDcseVDIEB4z7uMwcGBYWImKYOWi01pDYQslQjrWb2Xmh8EKsYbFQeXUtVIweDK8oVpWFwUsgxE_afstk15eqzot88gkIRnN_vlvQTIbrEzZAAAAAYYwpwkA")
