#RallsThon

import asyncio
import random

Ulodya = [
   "𓄂",
   "⇲",
   "𖦼",
   "❒", 
   "༕",
   "༗",
   "",
   "༗",
   "⌭",
]

@bot.on(
    admin_cmd(
       pattern="رموز", outgoing=True
    )
)
async def Ralls(zel):
   Ulo = random.choics(Ulodya)
   await zel.edit("**وجع انتظر...**")
   await asyncio.sleep(3)
   await eor(zel, Ulo)
