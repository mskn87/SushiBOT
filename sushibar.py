import discord
import logging
import configparser
import os

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# configファイルからTOKEN読み込み
conf = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), 'config.ini')
conf.read(path)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await tree.sync()

@tree.command(name="sushi", description="へいおまち！")
async def sushi_command(interaction: discord.Interaction):
    embed=discord.Embed(title="ハマチ",color=0xff0000)
    fname = 'sushi_hamachi.png'
    file = discord.File(fp=os.path.join(os.path.dirname(__file__), 'img', 'sushi_hamachi.png'), filename=fname, spoiler=False)
    embed.set_image(url=f"attachment://{fname}")#URLでEmbedに画像を貼る
    await interaction.response.send_message(file=file, embed=embed,ephemeral=True)
    print(f'コマンド実行！→{interaction.user}')
    #ephemeral=True→「これらはあなただけに表示されています」

token = conf['TOKEN']['token']
client.run(token, log_handler=handler)