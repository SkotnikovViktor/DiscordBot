import disnake
from disnake.ext import commands

CONSORED_WORDS = ["Блять","блять","сука"]

bot = commands.Bot(command_prefix="<",help_command=None,intents=disnake.Intents.all())

@bot.event
async def on_ready():
	print(f"Bot{bot.user} is ready work!")

@bot.event
async def on_message(message):
	for content in message.content.split():
		for consored_word in CONSORED_WORDS:
			if content==consored_word:
				await message.delete()
				await message.channel.send(f"{message.author.mention}Говорит плохое слово!")

bot.run("MTEwODgxNzg4MDg1NTg3MTU4MA.GpF2V6.lBVyh2jKe7tgknFwxBqGtKmaewWJhAsEEAzF9g")
