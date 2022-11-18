from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler


class TelegramBot():
    def __init__(self, config, logger):
        self.token = config['token']
        self.bot_name = config['name']
        self.bot_user = config['user']
        self.logger = logger

    def run(self):
        self.updater = Updater(self.token, use_context=True)

        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.dispatcher.add_handler(CommandHandler('help', self.help))

        self.updater.start_polling()
        self.logger.debug("run bot")

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text(
            "Enter the text you want to show to the user whenever they start the bot")
        self.logger.debug("start")

    def help(self, update: Update, context: CallbackContext):
        update.message.reply_text("Your Message")
        self.logger.debug("help")

