import requests


# 获取企业经纬度
def get_geocode(DOM):
    if not DOM:
        return 0, 0, 0

    the_url = "http://restapi.amap.com/v3/geocode/geo?key=b4b1a1eebd7c11db2923776c3d38412e&address=%s" % DOM
    the_r = requests.get(the_url, timeout=10)
    if the_r.status_code in ["200", "201", 200, 201]:
        the_j = the_r.json()["geocodes"][0]
        if "location" in the_j:
            lng, lat = the_j["location"].split(",")
            try:
                if float(lat) > 70:
                    lat, lng = lng, lat
            except:
                pass
            level = get_level(the_j["level"])
            return lat, lng, level
        else:
            return 0, 0, 0


def get_level(level):
    level_dict = ((0, "国家"), (1, "省"), (2, "市"), (3, "区县"),
                  (3, "开发区"), (3, "乡镇"), (3, "村庄"), (4, "热点商圈"), (5, "兴趣点"), (6, "门牌号"), (6, "单元号"), (5, "道路"),
                  (5, "道路交叉路口"), (5, "公交站台、地铁站"),
                  (0, "未知"))
    for k, v in level_dict:
        if level == v:
            return k


ent = '北京市怀柔区怀北镇怀北路３０８号'
name = get_geocode(ent)
print()
