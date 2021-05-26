from instabot import Bot
import time, os
bot = Bot()
bot.login(username=os.getenv('EMAIL_USER'), password=os.getenv('EMAIL_PASS'))

following = bot.get_user_following(username)
for i in following:
    bot.unfollow(i)
    time.sleep(2)

bot.logout()