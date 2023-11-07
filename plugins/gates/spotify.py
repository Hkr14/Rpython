from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import gather
from datetime import datetime, timedelta
from io import BytesIO
from math import atan2, cos, radians, sin, sqrt
from os import execvp
from random import randint
from re import findall
from re import sub as re_sub
from sys import executable
import aiofiles
import speedtest
import os
import requests
import time
import string
import random
import json
import requests
import time
import asyncio
from colored import fg, bg, attr
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 
@Client.on_message(filters.command(["spotify"], ["/", "."]))
async def xi(_, message: Message):
  

  
  def getRandomString(length):
    pool = string.ascii_lowercase + string.digits
    return "".join(random.choice(pool) for i in range(length))
    
  def getRandomText(length):
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))


  def generate():
    nick = getRandomText(8)
    passw = getRandomString(12)
    email = nick + "@" + "gmail" + ".com"

    headers = {
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-US",
        "App-Platform": "Android",
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "spclient.wg.spotify.com",
        "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
        "Spotify-App-Version": "8.6.72",
        "X-Client-Id": getRandomString(32)
    }

    payload = {
        "creation_point": "client_mobile",
        "gender": "male" if random.randint(0, 1) else "female",
        "birth_year": random.randint(1990, 2000),
        "displayname": nick,
        "iagree": "true",
        "birth_month": random.randint(1, 11),
        "password_repeat": passw,
        "password": passw,
        "key": "142b583129b2df829de3656f9eb484e6",
        "platform": "Android-ARM",
        "email": email,
        "birth_day": random.randint(1, 20)
    }

    r = requests.post(
        'https://spclient.wg.spotify.com/signup/public/v1/account/',
        headers=headers,
        data=payload)

    if r.status_code == 200:
        if r.json()['status'] == 1:
            text = f"""
Auto Spotify Created! ✅
🍏 Subscripcion-»  Free
🍏 Email-» <b>{email}</b>
🍏 Password-»<code>{passw}</code>"""

            return (text)
        else:
            #Details available in r.json()["errors"]
            #print(r.json()["errors"])
            return (False, "Could not create the account, some errors occurred")
    else:
        return (False,
                "Could not load the page. Response code: " + str(r.status_code))



  return await message.reply(generate())
    