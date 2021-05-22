import discord
import random
import openpyxl
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트 확인중...")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("테스트"):
        await message.channel.send("확인")
    if message.content.startswith("메이플"):
        await message.channel.send("스토리")
    if message.content == "$도움말":
        embed = discord.Embed(title="도움말", description="제작중...", color=0x62c1cc)  # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="가위바위보", value="`$가위`**,**`$바위`**,**`$보`", inline=False)
        embed.add_field(name="문의 넣는법", value="`$문의 566251769991135253 할말`**,**`설명`**,**`설명`**,**`설명`", inline=False)
        embed.add_field(name="소제목", value="`설명`**,**`설명`**,**`설명`**,**`설명`", inline=False)
        embed.add_field(name="소제목", value="`설명`**,**`설명`**,**`설명`", inline=False)
        embed.add_field(name="소제목", value="`설명`**,**`설명`**,**`설명`", inline=False)
        embed.add_field(name="제목", value="`흠`", inline=False)
        embed.set_footer(text="문의는 한구깃#")  # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed)  # embed를 포함 한 채로 메시지를 전송합니다.
        # await message.channel.send("할 말", embed=embed)  # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    if message.content == "$test":
        embed = discord.Embed(title="테스트용", description="https://www.youtube.com/watch?v=4xl9F2zEx34", color=0x62c1cc)
        embed.set_footer(text="")
        await message.channel.send(embed=embed)
    if message.content == "$가위" or message.content == "$바위" or message.content == "$보":
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            if message.content == "$가위":
                await message.channel.send("가위")
                await message.channel.send("비겼습니다")
            elif message.content == "$바위":
                await message.channel.send("가위")
                await message.channel.send("제가 졌습니다")
            else:
                await message.channel.send("가위")
                await message.channel.send("제가 이겼습니다")
        elif bot_response == 2:
            if message.content == "$가위":
                await message.channel.send("바위")
                await message.channel.send("제가 이겼습니다")
            elif message.content == "$바위":
                await message.channel.send("바위")
                await message.channel.send("비겼습니다")
            else:
                await message.channel.send("바위")
                await message.channel.send("제가 졌습니다")
        else:
            if message.content == "$가위":
                await message.channel.send("보")
                await message.channel.send("제가 졌습니다")
            elif message.content == "$바위":
                await message.channel.send("보")
                await message.channel.send("제가 이겼습니다")
            else:
                await message.channel.send("보")
                await message.channel.send("비겼습니다")
    if message.content.startswith("$도박"):
        l = 0
        while l <10000000:
            a = random.randint(1,100)
            b = random.randint(1,100)
            c = random.randint(1,100)
            sum  = a+b+c
            count = 0
            if sum >= 240:
                count += 1
            await message.channel.send(count)
            l += 1































































client.run("NzgxODk2NzYzMjQxNzkxNTQw.X8EUGw.p75VUKSv0OdpfVp3Stps53DgjEg")
