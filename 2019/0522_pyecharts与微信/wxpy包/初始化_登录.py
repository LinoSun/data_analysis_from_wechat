from wxpy import *

bot = Bot()

# 机器人自身账号
myself = bot.self

# 向文件传输助手发送信息
# bot.file_helper.send('lino is handsome')

print(bot.friends(update=True))