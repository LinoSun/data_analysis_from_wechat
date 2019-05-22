import re

from wxpy import Bot, Chat

# 获取好友
class Demo(Chat):
    @staticmethod
    def get_friend():
        bot = Bot(console_qr=False)
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

# 获取城市列表
def get_data():
    friend = Demo.get_friend()

    city_data = [d['city'] for d in friend if d['city']]

    city_dict = {}
    for city in city_data:

        if not re.sub("[a-z A-Z]", "", city):
            continue

        city_dict.setdefault(city, 0)
        city_dict[city] += 1

    city_list = []
    for key, value in city_dict.items():
        d = [key, value]
        city_list.append(d)

    return city_list

# 地理坐标图
def geo_base():
    city_data = get_data()
    print(city_data)



if __name__ == '__main__':

    geo_base()