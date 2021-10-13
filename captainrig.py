#!/usr/bin/python3
import discord
import logging
from phrases import *
from rigreboot import rebootHighwind, rebootTrailblazer, bootHighwind, bootTrailblazer

def is(keyword,name,text):
    return name in text.lower() and keyword in text.lower()



logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
high, trail = False, False
class MyClient(discord.Client):
    high = False
    trail = False
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
           
            if is('offline','highwind',text):
                if self.high:
                    self.high = False
                    return
                await message.channel.send(auto_highwind)
                logging.info('Rebooting highwind.')
                rebootHighwind(10)

            if is('offline','trailblazer',text):
                if self.trail:
                    self.trail = False
                    return
                await message.channel.send(auto_trailblazer)
                logging.info('Rebooting Trailblazer.')
                rebootTrailblazer(10)

            if is('offline','chariot',text):
                await message.channel.send(auto_chariot)
            if is('offline','orphan',text):
                await message.channel.send(auto_orphan)

        # User actions
        else:

            if is('reboot','highwind',text):
                if message.author.name == 'redeye':
                    await message.channel.send(master_highwind)
                else:
                    await message.channel.send(grunt_highwind)
                logging.info('Rebooting Highwind.')
                self.high = True
                rebootHighwind(10)
            elif 'highwind' in text.lower() and 'boot' in text.lower():
                if message.author.name == 'redeye':
                    await message.channel.send(master_highwind)
                else:
                    await message.channel.send(grunt_highwind)
                logging.info('Booting Highwind.')
                bootHighwind()

            if 'trailblazer' in text.lower() and 'reboot' in text.lower():
                if message.author.name == 'redeye':
                    await message.channel.send(master_trailblazer)
                else:
                    await message.channel.send(grunt_trailblazer)
                logging.info('Rebooting Trailblazer.')
                self.trail = True
                rebootTrailblazer(10)

            elif 'trailblazer' in text.lower() and 'boot' in text.lower():
                if message.author.name == 'redeye':
                    await message.channel.send(master_trailblazer)
                else:
                    await message.channel.send(grunt_trailblazer)
                logging.info('Booting Trailblazer.')
                bootTrailblazer()
            
            if 'chariot' in text.lower() and 'reboot' in text.lower():
                await message.channel.send(any_chariot)
            if 'orphan' in text.lower() and 'reboot' in text.lower():
                await message.channel.send(any_chariot)

with open('token') as f:
    token = f.readline()

client = MyClient()
client.run(token)

