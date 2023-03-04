import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "15823382"))
    API_HASH = os.environ.get("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6199650817:AAE9wyCls_CBBQwnzWgrRcKZRrSs7POiSR4")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5104293442")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "free_forwardr_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
