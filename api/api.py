from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from bot import bot

app = FastAPI()

@app.post("/")
async def handle_discord_webhook():
    await bot.process_commands()
    return PlainTextResponse("OK")
