# bot.py
import os
import random

import requests
from urllib.parse import urlencode
import base64
import webbrowser

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

auth_headers = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": "http://localhost:7777/callback",
    "scope": "user-library-read"
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

code = "insert your authorization code here"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=Intents.all())

# allow user to subscribe to the bot
# TODO: make this work
@bot.command(name='subscribe', help='Subscribe to the bot')
async def subscribe(ctx):
    # fsadf asdfa sdfa sdf adsf asdf ads f emma I hate it heres
    await ctx.send('subscribed!')

@bot.command(name='unsubscribe', help='Unubscribe from the bot')
async def unsubscribe(ctx):
    # fsadf asdfa sdfa sdf adsf asdf ads f emma I hate it here
    await ctx.send('unsubscribed!')

bot.run(TOKEN)


























# @bot.command(name='EMP', help='Flirts with Emma Paterson')
# async def EMP(ctx):
#     pickup_lines = [
#         "What’s your sign?",
#         "Do you like raisins? How do you feel about a date?",
#         "If I could rearrange the alphabet, I’d put ‘U’ and ‘I’ together.",
#         "Are you a parking ticket? Because you’ve got FINE written all over you.",
#         "Are you from Tennessee? Because you’re the only 10 I see!",
#         "Are you French? Because Eiffel for you.",
#         "I’m no photographer, but I can picture us together.",
#         "Feel my shirt. Know what it’s made of? Boyfriend material.",
#         "Are you Australian? Because you meet all of my koala-fications.",
#         "OMG. I was going to wear this exact same outfit tonight.",
#         "Are you a magician? When I look at you everything disappears.",
#         "There is something wrong with my cell phone. It doesn’t have your number in it.",
#         "Are you religious? Cause you’re the answer to all my prayers.",
#         "Do you believe in love at first sight — or should I walk by again?",
#         "Do you like coffee? Because I like you a latte.",
#         "Can I give you a hug to show you how soft my sweater is?",
#         "If a star fell from the sky every time I thought about you, then tonight the sky would be empty.",
#         "Is it hot in here? Or is it just you?",
#         "I don’t have a library card, but do you mind if I check you out?",
#         "Are you the sun? I’m about to get a sunburn looking at you.",
#         "Hey, tie your shoes! I don’t want you falling for anyone else.",
#         "Roses are red. Violets are blue. I didn’t know what perfect was until I met you.",
#         "Can I follow you where you’re going right now? Because my parents always told me to follow my dreams.",
#         "You look great right now. Do you know what else would look great on you? Me!",
#         "You dropped something. My jaw.",
#         "If you were words on a page, you’d be fine print.",
#         "There must be something wrong with my eyes, I can’t take them off you.",
#         "Are you a bank loan? Because you got my interest.",
#         "Somebody call the cops, because it’s got to be illegal to look that good!",
#         "Do you know why it doesn’t matter if there’s gravity or not? Because I’d still fall for you.",
#         "I must be a snowflake, because I’ve fallen for you.",
#         "Are you a keyboard ? Because you are my type.",
#         "Do you have a map? I just got totally lost in your eyes.",
#         "Are you an interior decorator? When I saw you the room became so beautiful.",
#         "Sweetness is my weakness.",
#         "You know what’s the worst thing that can happen to you right now? Me not dating you.",
#         "I know you’re busy today, but can you add me to your to-do list?",
#         "Has anyone ever told you how beautiful my eyes are?",
#         "If you were a steak you would be well done."
# #     ]

#     response = random.choice(pickup_lines)
#     print(response)
#     await ctx.send(response)
