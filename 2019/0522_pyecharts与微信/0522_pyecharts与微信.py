from wxpy import Bot, Chat

# 获取好友
class Demo(Chat):
    @staticmethod
    def get_friend():
        bot = Bot()
        friends = bot.friends(update=True)

        friend_data = []
        for friend in friends:
            if friend.sex == 1:
                sex = '男'
            elif friend.sex == 2:
                sex = '女'
            else:
                sex = ''
        friend_dic = {
            "city": friend.city,
            "province": friend.province,
            "sex": sex,
            "signature": friend.signature
        }
        friend_data.append(friend_dic)

        return friend_data
