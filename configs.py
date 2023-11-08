from os import path, getenv


class Config:
    API_ID = int(getenv('API_ID','13532780'))
    API_HASH = getenv('API_HASH','f73ffaec3acf05270cde1dc63c561ef0')
    BOT_TOKEN = getenv('BOT_TOKEN','5970810632:AAHvz8bWWXAo_18QOmmzlbFBxO7DToOUSWQ')

config = Config()
