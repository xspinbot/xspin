import sys
import asyncio

from bot.utils.polling import polling

def cli():
    commands = sys.argv

    if len(commands) == 2:
        if commands[1] == 'polling':
            asyncio.run(polling())
        else:
            print(f"Command '{commands[1]}' not found!\nCommands: polling\n\npython3 -m bot command")
    else:
        print(f"Command not entered!\n\nCommands: polling\n\npython3 -m bot command")
