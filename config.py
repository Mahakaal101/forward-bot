import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "26305247"))
    API_HASH = os.environ.get("API_HASH", "20ca7e6687c281e11782856c7efd0ff7")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6060605771:AAEqHZOy9gbjoCTYN8t-zGN6o8bHoTMe2OE")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5791145987")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Dipanshu_021:ad8920@cluster0.f7migc1.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQC1y84xwkP7kxhZXX4Yu5dxjZUAlmP97tiVYXK6QKH0medJ5DSeiT_nf3FjHL_9KZ5VAoUBtSDOKftmyWVRpJnhccL50Pyny9n_Vl-1ZUguEqfOwWksbQYJLsjcp2xCy4pKsePOH4GVYsoEnGM2x_5OENKT4vfoW3zPRF0cnvqVAyE_wvHfoz9_OQoU0WQ6ydqbTuoC-4AAnUrREqYe0yslLlTDtbSj2l3vPLmmsOm_rIg7zvkKGYr5G3ZA_0pg-XPi-ihldnOJIWcpJVikqdSqBA6ruKu59S9oGVZ34lAdP8mhKNtm2YbP7lPg29pKY4rkl5qcUumCVj3tDQzFgA4-AAAAATA9VkIA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001805905765"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "learningjgdfoighjnedvbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
