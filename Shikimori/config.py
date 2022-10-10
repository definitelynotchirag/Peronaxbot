# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

from Shikimori.vars import HEROKU_API_KEY, HEROKU_APP_NAME, REDIS_URL

def get_user_list(config, key):
    with open("{}/Senku/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 12335430  # integer value, dont use ""
    API_HASH = "2a9046339be3b90ec40891896b95f77e"
    BOT_TOKEN = "5756571846:AAF1XIJ7SwOrkpQm6p_1YgEuE7GoX6fu1qw"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1109460378  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "chirag57"
    SUPPORT_CHAT = "peronaxsupport"  # Your own group for support, do not add the @
    LOG_CHANNEL = (
        -1001795543122
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://bbiovhcz:I6YB-BEFAlMclvJNhAtzBLMMY8oE8K0P@satao.db.elephantsql.com/bbiovhcz"  # needed for any database modules
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "RO128OO27KM4BFJI"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "NJ20T2PMH1OH"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ERROR_LOG_CHANNEL = -1001795543122  # needed to make sure 'save from' messages persist
    HEROKU_API_KEY = "1d15e75b-c831-4a69-b3a8-b0743d662f3b"   # Your Heroku API key, get it from 'https://dashboard.heroku.com/account
    HEROKU_APP_NAME = (
        "peronatest"  # Enter the Heroku app name here (Must an exact same name with your input above)
    )
    ARQ_API = "KAWQFT-VKAEYR-AAMZCN-CKSEUZ-ARQ"
    APOD_API_KEY = "awoo"
    REDIS_URL = "redis://admin:A9325442737a@@redis-10041.c301.ap-south-1-1.ec2.cloud.redislabs.com:10041/bot-free-db"
    ANIME_NAME = "One Piece"
    START_MEDIA = "https://telegra.ph/file/2a965bf4dcd562ce4e9da.mp4"
    BOT_USERNAME = "perona_xbot"
    UPDATE_CHANNEL = "macnetwork7"
    ALIVE_MEDIA = "https://telegra.ph/file/2a965bf4dcd562ce4e9da.mp4"
    BOT_ID = 5756571846
    STATS_IMG = "awoo"
    NETWORK_USERNAME = "macnetwork7"
    NETWORK = "Mac"
    INLINE_IMG = "https://dthezntil550i.cloudfront.net/5y/latest/5y2207261412029340005917508/1280_960/b880d9ee-d293-41c6-8e6a-bb406136c28f.png"
    API_WEATHER = "awoo"
    OWNER_WELCOME_MEDIA = ""

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 12335430  # integer value, dont use ""
    API_HASH = "2a9046339be3b90ec40891896b95f77e"
    BOT_TOKEN = "5756571846:AAF1XIJ7SwOrkpQm6p_1YgEuE7GoX6fu1qw"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1109460378  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "chirag57"
    SUPPORT_CHAT = "peronaxsupport"  # Your own group for support, do not add the @
    LOG_CHANNEL = (
        -1001795543122
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://bbiovhcz:I6YB-BEFAlMclvJNhAtzBLMMY8oE8K0P@satao.db.elephantsql.com/bbiovhcz"  # needed for any database modules
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "RO128OO27KM4BFJI"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "NJ20T2PMH1OH"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ERROR_LOG_CHANNEL = -1001795543122 # needed to make sure 'save from' messages persist
    HEROKU_API_KEY = "1d15e75b-c831-4a69-b3a8-b0743d662f3b"   # Your Heroku API key, get it from 'https://dashboard.heroku.com/account
    HEROKU_APP_NAME = (
        "peronatest"  # Enter the Heroku app name here (Must an exact same name with your input above)
    )
    ARQ_API = "KAWQFT-VKAEYR-AAMZCN-CKSEUZ-ARQ"
    APOD_API_KEY = "awoo"
    REDIS_URL = "redis://admin:A9325442737a@@redis-10041.c301.ap-south-1-1.ec2.cloud.redislabs.com:10041/bot-free-db"
    ANIME_NAME = "One Piece"
    START_MEDIA = "https://telegra.ph/file/2a965bf4dcd562ce4e9da.mp4"
    BOT_USERNAME = "perona_xbot"
    UPDATE_CHANNEL = "macnetwork7"
    ALIVE_MEDIA = "https://telegra.ph/file/2a965bf4dcd562ce4e9da.mp4"
    BOT_ID = 5756571846
    STATS_IMG = "awoo"
    NETWORK_USERNAME = "macnetwork7"
    NETWORK = "Mac"
    INLINE_IMG = "https://dthezntil550i.cloudfront.net/5y/latest/5y2207261412029340005917508/1280_960/b880d9ee-d293-41c6-8e6a-bb406136c28f.png"
    API_WEATHER = "awoo"
    OWNER_WELCOME_MEDIA = ""
    AUTH_USERS = "1109460378"
    TG_BOT_TOKEN = "5756571846:AAF1XIJ7SwOrkpQm6p_1YgEuE7GoX6fu1qw"
    APP_ID = "12335430"