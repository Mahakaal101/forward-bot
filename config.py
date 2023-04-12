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
    SESSION = os.environ.get("SESSION", "BQAL7OVbfMurYfUeMU0GJ6YSImwcBHIeV5l-UwJplbP7Xnp9rQjHOd50ouM0cmNokfyMqzHfm1OLkASGrr_nQTwTIgej3OVQFFNrAvfPeLqOl0eQRbK_q_GLww4OC3NElJYnkjRrV3H7ocK3BA1YG3r-sZPigYfSxZeC_4Mvho9TWRhygXCqu4kY0xVAr5RD71W4e1aPH-kVB9AfO7L54c3oMTfXodsT4WZPx7alyfPZJ7_-29LsAI9zlKgH_5j144BhimqHGwH3DcmifpvOm-JORPjDcIwwvVZGev8d8MDPq0Jweip8vzZW28S5lLKktJqDyktNYhZsJhOE9oNY2EB4AAAAATMiN8EA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001805905765"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "learningjgdfoighjnedvbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
