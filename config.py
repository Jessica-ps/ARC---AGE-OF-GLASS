import logging
from os import environ
from dotevn import load_dotenv
load_dotenv

BACKEND = 'Discord'  
BOT_IDENTITY = {'token' : environ.get('DISCORD_TOKEN')
}
BOT_ADMINS = (environ.get('BOT_ADMIN'), )  
BOT_PREFIX = '!'
BOT_PREFIX_OPTIONAL_ON_CHAT = True

BOT_DATA_DIR = r'data'
BOT_EXTRA_PLUGIN_DIR = r'plugins'
BOT_EXTRA_PLUGIN_DIR = r'Backend'

BOT_LOG_FILE = r'errbot.log'
BOT_LOG_LEVEL = logging.DEBUG
