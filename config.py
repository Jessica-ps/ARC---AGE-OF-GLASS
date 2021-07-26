import logging  
from os import environ

BACKEND = 'Discord'  
BOT_IDENTITY = {
'token' : environ.get('DISCORD_TOKEN')
}
BOT_ADMINS = ['Jéssica#7541', ]

BOT_DATA_DIR = r'data'
BOT_EXTRA_PLUGIN_DIR = r'plugins'
BOT_EXTRA_BACKEND_DIR = r'backend'

BOT_LOG_FILE = r'errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@CHANGE_ME', ) 