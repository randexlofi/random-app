from datetime import datetime

APP_VER = '0.0.1a'
BOT_TOKEN = 'BOTTOKEN'
APP_CHANNEL_WH = 'DISCORDWEBHOOK'

def GetFullTime():
    current_datetime = datetime.now()

    # Format the date and time
    formatted_date_time = current_datetime.strftime("[%d-%m-%Y %H:%M:%S]")

    return formatted_date_time
