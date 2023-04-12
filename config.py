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
    SESSION = os.environ.get("SESSION", "BQANlmCrRRehNkWQU5M5uZ0rESjoItC0L3sEETPxH-oWshgPe5hprsUByc8wlg7SLdkrp5_ARqC8VQ4I0JlJw44JsDK72NYsi8FQ_rfF90gPO-1-m7zrIM_06B1Uu2IhJBySBrLIClZ_h8lHVZyVpSQ-fOUEZ5TEefrEVuotznty-xk78pctOZZJcYxdN_KfEI9qf6VRalBM16Lx-NTNjsZrMpgHKAfwyb2omTienMdoIQbC20cZQ0tqfz33czRLE9Ud8DTckEtVjjeG20XQlsBXlvr16-e6KONulYhtuw_Vxrk_R-iLbBKjsEuAfzPz7XMX5-k1FXYaXkKtuXd09tMiAAAAATMiN8EA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001805905765"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "learningjgdfoighjnedvbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
