from os import path, getenv


class Config:
    API_ID = int(getenv('API_ID','13532780'))
    API_HASH = getenv('API_HASH','f73ffaec3acf05270cde1dc63c561ef0')
    BOT_TOKEN = getenv('BOT_TOKEN','5970810632:AAHDy3TBzd4nm9scBgeDfQyoNUIsDxeI1L0')

config = Config()
