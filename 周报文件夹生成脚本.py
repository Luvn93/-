import datetime
import os

dir_path = "C:\\Users\\yu297\\Desktop\\date\\"


def exist(path):
    if not os.path.exists(path):
        os.mkdir(path)


i = 0
day = datetime.datetime.today()
interval = datetime.timedelta(days=1)
name1 = str(day.date()).replace("-", "")

while i < 365:

    week = datetime.datetime.weekday(day)

    if week == 0:
        name1 = str(day.date()).replace("-", "")
    if week == 6:
        name2 = str(day.date()).replace("-", "")
        name_path = os.path.join(dir_path, '%s' % name1+"-"+name2)
        # print(name_path)
        exist(name_path)

    day += interval
    i += 1
