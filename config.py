import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):

    # Client Config 
    API_ID = int(os.environ.get('API_ID', '23685822')) # ⚠️ Required
    API_HASH = os.environ.get('API_HASH', 'ff0572e13ff2f63a50f6dc707e0c4c9f') # ⚠️ Required
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '') # ⚠️ Required

    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Leviabcd:VL0RUYZHI0xrwDvz@cluster0.0cvcei0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # ⚠️ Required

    # Other Config 
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "request_accept_autobot") # ⚠️ Required
    BOT_UPTIME  = time.time()
    OWNER = int(os.environ.get('OWNER', '1018033649')) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003043625840")) # ⚠️ Required
    APPROVED_WELCOME_TEXT = os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYou're Auto Approved. ✅")
    LEAVING_BY_TEXT = os.environ.get("APPROVED_WELCOME_TEXT", "👋 Bye {mention} !\nSee You Soon by {title}\n\nYou Left. ⛔")
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1001648037641') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None 

    # Web response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    PORT = int(os.environ.get("PORT", "8080"))

class Txt(object):

    START_MSG = """
🦁 Hᴇʟʟᴏ {} !,
I'ᴍ ᴀɴ ᴀᴜᴛᴏ Aᴘᴘʀᴏᴠᴀʟ Bᴏᴛ (Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛ)

I ᴄᴀɴ ᴀᴘᴘʀᴏᴠᴇ ᴜsᴇʀs ɪɴ Gʀᴏᴜᴘ ᴏʀ Cʜᴀɴɴᴇʟs. Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ 💬
"""
