# Self made
import asci
import discord_bot as dBot
import requests_main as reqMain
import settings
import webhookManager as whM

import os
import time
import tests

while True:
    usr = input('user: ')
    pwd = input('pwd: ')

    if usr == 'admin' and pwd == 'admin':
        os.system('cls')
        _hostname, _ip_address = reqMain.GetUserIP()
        whM.SendNormalMessage(settings.APP_CHANNEL_WH,
        f'''Login information for {usr}!
`DESKTOP:` **{_hostname}**
`ADDRESS:` **{_ip_address}**

*`App version: {settings.APP_VER}`*
''',
        usr)
        break
    else:
        opt = input('Your user or password is not correr, wanna try again? [y/n]: ')
        if opt.lower() != 'y':
            outpa = ''
            for i in range(3):
                outpa += '.'
                print(f'Closing the app{outpa}', end='\r')
                time.sleep(1)
                i+=1
            quit()

asci.AppMenu()
while True:
    inpt = input('>')

    if inpt.lower() == "help":
        print(
'''
 OVERVIEW
  HELP            [shows this]
  CLR             [clear the console]
  QUIT            [close the app]
 
 DISCORD
  STRBOT          [start the bot]
  STPBOT          [stop the bot]
  DSPLOG          [display the chat log console]

 MISC
  GETADR          [display the current user machine name/adress]

For more adicional help type "help (command)"
'''
)
    elif inpt.lower() == 'quit':
        exit()
    elif inpt.lower() == "clr":
        opt = input('Are you sure you wanna clear the console [y/n]: ')
        if opt.lower() == 'y':
            os.system('cls')
            asci.AppMenu()
    elif inpt.lower() == "strbot":
        try:
            dBot.RunBot()
        except Exception as e:
            print(f'An error ocurred while trying to start the bot: {e}')
    elif inpt.lower() == "getadr":
        _hostname, _ip_address = reqMain.GetUserIP()
        print(f'''
   HOSTNAME          ADDRESS
   {_hostname}   {_ip_address}
''')
    elif inpt.lower() == 'test':
        try:
            print('\n')
            tests.LoadingBar(barAmount=15, loadText='Loading', backChar='░', frontChar='█')
            print('\n')
        except Exception as e:
            print(e)
