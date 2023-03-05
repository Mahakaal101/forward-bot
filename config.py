import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "15823382"))
    API_HASH = os.environ.get("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6199650817:AAE9wyCls_CBBQwnzWgrRcKZRrSs7POiSR4")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5104293442")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Dipanshu_021:ad8920@cluster0.f7migc1.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQC1y84xwkP7kxhZXX4Yu5dxjZUAlmP97tiVYXK6QKH0medJ5DSeiT_nf3FjHL_9KZ5VAoUBtSDOKftmyWVRpJnhccL50Pyny9n_Vl-1ZUguEqfOwWksbQYJLsjcp2xCy4pKsePOH4GVYsoEnGM2x_5OENKT4vfoW3zPRF0cnvqVAyE_wvHfoz9_OQoU0WQ6ydqbTuoC-4AAnUrREqYe0yslLlTDtbSj2l3vPLmmsOm_rIg7zvkKGYr5G3ZA_0pg-XPi-ihldnOJIWcpJVikqdSqBA6ruKu59S9oGVZ34lAdP8mhKNtm2YbP7lPg29pKY4rkl5qcUumCVj3tDQzFgA4-AAAAATA9VkIA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001738753445"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "free_forwardr_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
