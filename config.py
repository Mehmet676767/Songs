import os

class Config:
    API_ID = int(os.environ.get("API_ID", "25114508")) #Karışmayın
    API_HASH = os.environ.get("API_HASH", "993ccdfe81548dade420e81bcd6807ce") #Karışmayın
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7196374262:AAG5fSCBpl1v89a26uuQxu2_UIpP7c0yd6c") #Botunuzun Tokenini Girin .  
