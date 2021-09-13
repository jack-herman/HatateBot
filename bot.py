import json
import discord

with open('config.json') as f:
    config = json.load(f)
    
TOKEN = config['BOT_TOKEN']
puppet_list = {}

client = discord.Client()

def set_dict():
    dict_keys = ['name', 'type1', 'type2', 'hp', 'foatk', 'fodef', 'spatk', 'spdef', 'spd', 'bst', 'cost', 'ability1', 'ability2']
    with open('puppets.txt') as fi:
     line = fi.readline()
     while line != '':
         values = {}
         puppet = line.split('  ', 12)
         # print(puppet)
         for key in dict_keys:
            values[key] = puppet[dict_keys.index(key)]
         puppet_list[puppet[0].lower()] = values
         line = fi.readline()


@client.event
async def on_ready():    
    set_dict()
    print('Bot has logged in')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hatatebot') or client.user in message.mentions:
        author = message.author
        commands = message.content.split(' ', 2)
        del commands[0]
        if commands[0].lower() == 'puppet': 
            puppet = puppet_list[commands[1].lower()]
            msg = f"""
                    {puppet['name']}: 
                    Type 1: {puppet['type1']} 
                    Type 2: {puppet['type2']} 
                    HP: {puppet['hp']} 
                    Focus Attack: {puppet['foatk']} 
                    Focus Defense: {puppet['fodef']} 
                    Spread Attack: {puppet['spatk']}
                    Spread Defense: {puppet['spdef']}
                    Speed: {puppet['spd']}
                    BST: {puppet['bst']}
                    Cost: {puppet['cost']}
                    Ability 1: {puppet['ability1']}
                    Ability 2: {puppet['ability2']}
                    """
            await message.channel.send(msg)
        elif commands[0].lower() == 'help':
            msg = """
                The current available HatateBot commands are:\n
                - Hatatebot puppet <puppet>\n
                    - Shows the name, type, stats, and abilities of the requested puppets.\n
                    - Input puppet as <first letter of style> + <puppet name> e.g. EReimu\n
                    - Capitalization does not matter\n
                - Hatatebot help\n
                    - Shows this help menu\n
                """
            await message.channel.send(msg)

client.run(TOKEN)
