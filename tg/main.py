import feedparser
import logging
from datetime import datetime
from datetime import date
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'madarchod {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )
def rss(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    NewsFeed = feedparser.parse("https://nyaa.si/?page=rss")
    f = 0
    big_string = " "
    for x in NewsFeed.entries:
        if f >= 10:
            break
        f = f + 1
        big_string += f"Link is {x.id}\n\n"
    print(big_string)
    update.message.reply_markdown_v2(
        f'top 10 rss feeds are {big_string}',
        reply_markup=ForceReply(selective=True),
    )

def time(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y")
    update.message.reply_markdown_v2(
        fr'today\'s date is {date_time} \!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5577064578:AAEP5z0qLsTOkda1XzDzAxciy_OdInGrDxI")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("FUCK", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("now", time))
    dispatcher.add_handler(CommandHandler("rss", rss))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
