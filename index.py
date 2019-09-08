from piazza_api import Piazza
import datetime, sched, time
from gpiozero import LED
led = LED(17)
p = Piazza()
p.user_login("cummin26@purdue.edu","Lavalamp#02")
user_profile = p.get_user_profile()
cs180 = p.network('j6dkyqj34gm3rw')
s = sched.scheduler(time.time, time.sleep)


def updateLight():
    posts = cs180.iter_all_posts(limit=10)
    now = datetime.datetime.now()
    valid = False
    for i in posts:
        if((datetime.datetime.now() - datetime.timedelta(minutes=30)) < datetime.datetime.strptime(i["created"],"%Y-%m-%dT%H:%M:%SZ")):
            led.on()
            valid = True
    if(not valid):
        led.off()
