#!/usr/bin/python3
import discord
import logging
from rigreboot import rebootHighwind, rebootTrailblazer, bootHighwind, bootTrailblazer

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
        if message.author.name == 'Hive Bot':
            if 'highwind' in text.lower() and 'offline' in text.lower():
                if self.high:
                    self.high = False
                    return
                await message.channel.send('Blimey! Highwind full sail lads!')
                logging.info('Rebooting highwind.')
                rebootHighwind(5)
            elif 'trailblazer' in text.lower() and 'offline' in text.lower():
                if self.trail:
                    self.trail = False
                    return
                await message.channel.send('Scurvy dog! Trailblazer full speed ahead matey!')
                logging.info('Rebooting Trailblazer.')
                rebootTrailblazer(5)
            elif 'chariot' in text.lower() and 'offline' in text.lower():
                await message.channel.send('Despicable! Chariot be damned!')
            elif 'orphan' in text.lower() and 'offline' in text.lower():
                await message.channel.send('Thar she blows! And a right foul orphan ye arrr!')
        else:
            if 'highwind' in text.lower() and 'reboot' in text.lower():
                if message.author.name == 'redeye':
                    await message.channel.send('Why yes master! As you command! Highwind full sail, put yer back into it lads!')
                else:
                    await message.channel.send("Watch yer tongue ye wench! I'll have it fer stew! Ye herd'im lads...")
                logging.info('Rebooting Highwind.')
                self.high = True
                rebootHighwind(5)
            elif 'highwind' in text.lower() and 'boot' in text.lower():
                if message.author.name == 'redeye':
                    await message.channel.send('Why yes master! As you command! Highwind full sail, put yer back into it lads!')
                else:
                    await message.channel.send("Watch yer tongue ye wench! I'll have it fer stew! Ye herd'im lads...")
                logging.info('Booting Highwind.')
                bootHighwind()
            if 'trailblazer' in text.lower() and 'reboot' in text.lower():
                if message.author.name == 'redeye':
                    await message.channel.send('Oh senpai! I am not worthy of your gaze! Trailblazer full speed ahead, drop the sails ye scalliwags!')
                else:
                    await message.channel.send("May Davy Jones claim ye wretched soul! Make haste lads...")
                logging.info('Rebooting Trailblazer.')
                self.trail = True
                rebootTrailblazer(5)
            elif 'trailblazer' in text.lower() and 'boot' in text.lower():
                if message.author.name == 'redeye':
                    await message.channel.send('Oh senpai! I am not worthy of your gaze! Trailblazer full speed ahead, drop the sails ye scalliwags!')
                else:
                    await message.channel.send("May Davy Jones claim ye wretched soul! Make haste lads...")
                logging.info('Booting Trailblazer.')
                bootTrailblazer()
            if 'chariot' in text.lower() and 'reboot' in text.lower():
                await message.channel.send("HARHARHAR, yo ho ho! Quite the tale ye spin.")
            if 'orphan' in text.lower() and 'reboot' in text.lower():
                await message.channel.send("Ye landlubbers will hange the jib or I'll hang'em from the Yardam!")

client = MyClient()
client.run('ODkyMTg4NjY1MDg4OTk1MzI4.YVJRcQ.bu6_Va-GLbyodDW-1EC-aBrDlok')

