# coding: utf-8

import discord
from os import getenv

client = discord.Client()

# 起動時処理
@client.event
async def on_ready():
    print("Ready!")
    for channel in client.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):
    print("in on_voice_state_update")
    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        print("入室ステータスが変更された")
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(921953088359759892)

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [921941742494830685]

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けました！")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")


# 取得したトークンを「TOKEN_HERE」の部分に記入
token = getenv('DISCORD_BOT_TOKEN')

print("token:", token)
client.run(token)
