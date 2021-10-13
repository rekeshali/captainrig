#!/usr/bin/python3
import asyncio
import discord
import logging
from phrases import *
from rigreboot import rebootHighwind, rebootTrailblazer, bootHighwind, bootTrailblazer
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

def iskey(keyword,name,text):
    return name in text.lower() and keyword in text.lower()

class MyClient(discord.Client):
    booting_high = False
    booting_trail = False
    async def on_ready(self):
        logging.info('Logged on as %s.'%self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        text = message.content
        logging.info('%s: %s'%(message.author.name,text))
        
        # Automatic actions
        if message.author.name == 'Hive Bot':
            # Turn off booting flag when online
            if iskey('online','highwind',text):
                self.booting_high = False
            elif iskey('online','trailblazer',text):
                self.booting_trail = False
           
            # Makereboot decisions if turned offline
            elif iskey('offline','highwind',text):
                if self.booting_high: # User initiated
                    return
                else:
                    self.booting_high = True # Assume Hive initiated
                    await asyncio.sleep(600) # Wait to see if Hive has it covered
                    if self.booting_high: # Hive did not get to it
                        await message.channel.send(auto_highwind)
                        logging.info('Rebooting highwind.')
                        rebootHighwind(10)

            elif iskey('offline','trailblazer',text):
                if self.booting_trail: # User initiated
                    return
                else:
                    self.booting_trail = True # Assume Hive initiated
                    await asyncio.sleep(600) # Wait to see if Hive has it covered
                    if self.booting_trail: # Hive did not get to it
                        await message.channel.send(auto_trailblazer)
                        logging.info('Rebooting trailblazer.')
                        rebootTrailblazer(10)

            elif iskey('offline','chariot',text):
                await message.channel.send(auto_chariot)
            elif iskey('offline','orphan',text):
                await message.channel.send(auto_orphan)

        # User actions
        else:

            if iskey('reboot','highwind',text):
                if message.author.name == 'redeye':
                    await message.channel.send(master_highwind)
                else:
                    await message.channel.send(grunt_highwind)
                logging.info('Rebooting Highwind.')
                self.booting_high = True
                rebootHighwind(10)
            elif iskey('boot','highwind',text):
                if message.author.name == 'redeye':
                    await message.channel.send(master_highwind)
                else:
                    await message.channel.send(grunt_highwind)
                logging.info('Booting Highwind.')
                bootHighwind()

            elif iskey('reboot','trailblazer',text):
                if message.author.name == 'redeye':
                    await message.channel.send(master_trailblazer)
                else:
                    await message.channel.send(grunt_trailblazer)
                logging.info('Rebooting Trailblazer.')
                self.booting_trail = True
                rebootTrailblazer(10)
            elif iskey('boot','trailblazer',text):
                if message.author.name == 'redeye':
                    await message.channel.send(master_trailblazer)
                else:
                    await message.channel.send(grunt_trailblazer)
                logging.info('Booting Trailblazer.')
                bootTrailblazer()
            
            elif iskey('reboot','chariot',text):
                await message.channel.send(any_chariot)
            elif iskey('reboot','orphan',text):
                await message.channel.send(any_orphan)

with open('token') as f:
    token = f.readline()

client = MyClient()
client.run(token)

