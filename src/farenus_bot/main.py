from farenus_bot import bot
from farenus_bot import config


def main():
    bot.bot.run(config.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
