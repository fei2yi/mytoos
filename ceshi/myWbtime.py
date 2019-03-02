import time, re

minute = 1000 * 60
hour = minute * 60
day = hour * 24
halfamonth = day * 15
month = day * 30


def getDateDiff(dateTimeStamp):
    if ' ' in dateTimeStamp:
        idata = time.strptime(dateTimeStamp, "%Y-%m-%d %H:%M:%S")
        idata = int(round(time.mktime(idata) * 1000))
    else:
        idata = dateTimeStamp
    now = int(round(time.time() * 1000))
    diffValue = now - idata
    if diffValue < 0:
        result = "时间错误！"
    else:
        monthC = diffValue // month
        weekC = diffValue // (7 * day)
        dayC = diffValue // day
        hourC = diffValue // hour
        minC = diffValue // minute
        if monthC >= 1:
            result = str(monthC) + "个月前"
        elif weekC >= 1:
            result = str(weekC) + "周前"
        elif dayC >= 1:
            if dayC == 1:
                if ' ' in dateTimeStamp:
                    ti = dateTimeStamp.split()[-1].split(':')[:-1]
                    ti = ':'.join(ti)
                    result = "昨天 " + ti
                else:
                    result = "昨天"
            else:
                result = str(dayC) + "天前"
        elif hourC >= 1:
            result = str(hourC) + "小时前"
        elif minC >= 1:
            result = str(minC) + "分钟前"
        else:
            result = "刚刚"
        ss = re.findall("\d+", result)[0]
        if ss and int(ss) == 2:
            result = '两' + result[1:]
    return result


if __name__ == '__main__':
    print(getDateDiff('2018-12-23 03:08:14'))
