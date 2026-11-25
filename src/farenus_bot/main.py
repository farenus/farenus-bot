from farenus_bot import bot
from farenus_bot import config


def main():
    bot.Bot().run(config.DISCORD_TOKEN, root_logger=True)


if __name__ == "__main__":
    main()
