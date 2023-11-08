from os import path, getenv


class Config:
    API_ID = int(getenv('API_ID','13532780'))
    API_HASH = getenv('API_HASH','f73ffaec3acf05270cde1dc63c561ef0')
    BOT_TOKEN = getenv('BOT_TOKEN','5970810632:AAFVe6VCL6kNBJeQOXWm4PtzjeIW7fLXxZc')

config = Config()
