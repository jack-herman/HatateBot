import json
import discord

with open('config.json') as f:
    config = json.load(f)
    
TOKEN = config['BOT_TOKEN']
puppet_list = {}
ability_list = {}
skill_list = {}
item_list = {}

client = discord.Client()

def set_puppets():
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

def set_abilities():
    with open('AbilityData.csv') as fi:
        line = fi.readline()
        while line != '':
            ability = line.split('  ')
            ability_list[ability[0].lower()] = ability[-1]
            line = fi.readline()

def set_items():
    with open('ItemData.csv') as fi:
        line = fi.readline()
        while line != '':
            item = line.split('  ')
            item_list[item[0].lower()] = item[-1]
            line = fi.readline()

def set_skills():
    with open('SkillData.csv') as fi:
        line = fi.readline()
        while line != '':
            skill = line.split('  ')
            skill_list[skill[0].lower()] = skill[-1]
            line = fi.readline()

def set_dict():
    set_puppets()
    set_abilities()
    set_items()
    set_skills()


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
        elif commands[0].lower() == 'ability':
            msg = f"{commands[1]}: {ability_list[commands[1].lower()]}"
            await message.channel.send(msg)
        elif commands[0].lower() == 'item':
            msg = f"{commands[1]}: {item_list[commands[1].lower()]}"
            await message.channel.send(msg)
        elif commands[0].lower() == 'skill':
            msg = f"{commands[1]}: {skill_list[commands[1].lower()]}"
            await message.channel.send(msg)
        elif commands[0].lower() == 'help':
            msg = """
                The current available HatateBot commands are:\n
                - Hatatebot puppet <puppet>\n
                    - Shows the name, type, stats, and abilities of the requested puppets.\n
                    - Input puppet as <first letter of style> + <puppet name> e.g. EReimu\n
                    - Capitalization does not matter\n
                - Hatatebot ability <ability>\n
                    - Shows the description of the inputted ability\n
                    - Capitalization and spacing does not matter\n
                    - Punctuation does matter for inputs\n
                - Hatatebot item <item>\n
                    - Shows the description of the inputted item\n
                    - Capitalization and spacingdoes not matter\n
                    - Puncuation does matter for inputs\n
                - Hatatebot skill <skill>\n
                    - Shows the description of the inputted skill\n
                    - Capitalization and spacing does not matter\n
                    - Punctuation does matter for inputs\n
                - Hatatebot help\n
                    - Shows this help menu\n


                This Bot is free and open-source, it can be forked from https://github.com/jack-herman/HatateBot.
                Hatatebot is graciously hosted by maugrift.com
                """
            await message.channel.send(msg)

client.run(TOKEN)
