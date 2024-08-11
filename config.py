import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21827365"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8ce3a335da4143ea22c5305782cef359")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://torneeem:CLECq2ASbmdDuVbn@cluster0.7r3sw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
