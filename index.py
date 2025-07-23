import asyncio
from pyrogram import Client, filters
import aiohttp
import json

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

API_ID = config["api_id"]
API_HASH = config["api_hash"]
TELEGRAM_CHANNEL = config["telegram_channel"]
DISCORD_WEBHOOK_URL = config["discord_webhook_url"]
EMBED_CONFIG = config.get("embed", {})

app = Client("tg2dc", api_id=API_ID, api_hash=API_HASH)

async def send_to_discord(text):
    embed = {
        "description": text,
    }
    for key in ["title", "color", "author", "footer"]:
        if key in EMBED_CONFIG:
            embed[key] = EMBED_CONFIG[key]
    payload = {"embeds": [embed]}
    async with aiohttp.ClientSession() as session:
        async with session.post(DISCORD_WEBHOOK_URL, json=payload) as resp:
            if resp.status not in (200, 204):
                print(f"Ошибка отправки в Discord: {resp.status}")

@app.on_message(filters.chat(TELEGRAM_CHANNEL))
def forward(client, message):
    text = message.text or message.caption or "[нет текста]"
    asyncio.create_task(send_to_discord(text))

if __name__ == "__main__":
    app.run() 
