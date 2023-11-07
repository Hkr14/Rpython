import requests 
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["bin"], ["/", "."]))
async def cmds(client, message):
  
        
            BIN = message.text[len("/bin"): 11]

            if len(BIN) < 7:
                return await message.reply("<i>❌ formato:<code>/bin 456789</code></i>")
            if not BIN:
                return await message.reply("<i>❌ formato: <code>/bin 456789</code></i>")
            inputm = message.text.split(None, 1)[1]
            bincode = 6
            BIN = inputm[:bincode]
            req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()
            if 'bin' not in req:
                await message.reply_text(f'<i>❌ error bin no encontrado <code>{BIN} </code></i>')
                
            else:
                brand = req['brand']
                country = req['country']
                country_name = req['country_name']
                country_flag = req['country_flag']
                country_currencies = req['country_currencies']
                bank = req['bank']
                level = req['level']
                typea  = req['type']
                username= message.from_user.username
                await message.reply_text(f"""
               <b>
[ϟ] Bin Lookup
━━━━━━━━━━━━━━━
[Ϟ] Bin: <code>{BIN}</code> 
[Ϟ] Info: {brand}-{typea}-{level}
[Ϟ] Bank: {bank}
[Ϟ] Country: {country_name} {country_flag}-{country_currencies}
━━━━━━━━━━━━━━━
Checked By: {username}</b>

                """)

    