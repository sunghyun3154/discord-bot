from os import name

import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("/도움말 ( 성현 봇 )")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("/도움말"):
        await message.channel.send("```css\n[ 울산 봇 명령어 목록 ]```\n```/서버주소\n/서버법\n/관리자명단```\nBot made by 성현")
    if message.content.startswith("/서버주소"):
        await message.channel.send("52.231.10.188")
    if message.content.startswith("/서버법"):
        await message.channel.send("표기방법 조사 중")
    if message.content.startswith("/관리자명단"):
        await message.channel.send("```css\n[ 울산 서버 관리자명단 ]```\n```\n총관리자 Black_Net\n부총관리자 Hoya\n관리자 John Wick\n관리자 성현\n서버 개발팀 O-GU\n서버 개발팀 Tencheot\n인게임 관리자 dalki1404\n인게임 관리자 Roly_Poly\n인게임 관리자 바다(kocom9908)\n뉴비도우미 DOC\n뉴비도우미 Seabom```")



client.run("NjE0MzU2MDUwNTc3MTk1MDA5.XV-bxQ.bI1Q6aUlwlOoFJ46Ct68VmSB7-Y")