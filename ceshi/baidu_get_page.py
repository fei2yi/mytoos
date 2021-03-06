import requests
from parsel import Selector

sess = requests.session()


def get_url_by_name(wd=None):
    while True:
        url = 'https://www.baidu.com'
        sess.get(url)
        url = 'http://www.baidu.com/s?ie=utf-8&fr=bks0000&wd={}'.format(wd)
        res = sess.get(url)
        resp = Selector(res.text)
        url = resp.xpath('//h3/a/@href').extract_first()
        if not url:
            continue
        url = url.replace('http://', 'https://')
        res = sess.get(url, allow_redirects=False)
        url = res.headers['location']
        return url


if __name__ == '__main__':
    all_city = ['上海市',
                '北京市',
                '广州市',
                '深圳市',
                '成都市',
                '杭州市',
                '重庆市',
                '武汉市',
                '苏州市',
                '西安市',
                '天津市',
                '南京市',
                '郑州市',
                '长沙市',
                '沈阳市',
                '青岛市',
                '宁波市',
                '东莞市',
                '无锡市',
                '昆明市',
                '大连市',
                '厦门市',
                '合肥市',
                '佛山市',
                '福州市',
                '哈尔滨市',
                '济南市',
                '温州市',
                '长春市',
                '石家庄市',
                '常州市',
                '泉州市',
                '南宁市',
                '贵阳市',
                '南昌市',
                '南通市',
                '金华市',
                '徐州市',
                '太原市',
                '嘉兴市',
                '烟台市',
                '惠州市',
                '保定市',
                '台州市',
                '中山市',
                '绍兴市',
                '乌鲁木齐市',
                '潍坊市',
                '兰州市',
                '珠海市',
                '镇江市',
                '海口市',
                '扬州市',
                '临沂市',
                '洛阳市',
                '唐山市',
                '呼和浩特市',
                '盐城市',
                '汕头市',
                '廊坊市',
                '泰州市',
                '济宁市',
                '湖州市',
                '江门市',
                '银川市',
                '淄博市',
                '邯郸市',
                '芜湖市',
                '漳州市',
                '绵阳市',
                '桂林市',
                '三亚市',
                '遵义市',
                '咸阳市',
                '上饶市',
                '莆田市',
                '宜昌市',
                '赣州市',
                '淮安市',
                '揭阳市',
                '沧州市',
                '商丘市',
                '连云港市',
                '柳州市',
                '岳阳市',
                '信阳市',
                '株洲市',
                '衡阳市',
                '襄阳市',
                '南阳市',
                '威海市',
                '湛江市',
                '包头市',
                '鞍山市',
                '九江市',
                '大庆市',
                '许昌市',
                '新乡市',
                '宁德市',
                '西宁市',
                '宿迁市',
                '菏泽市',
                '蚌埠市',
                '邢台市',
                '铜陵市',
                '阜阳市',
                '荆州市',
                '驻马店市',
                '湘潭市',
                '滁州市',
                '肇庆市',
                '德阳市',
                '曲靖市',
                '秦皇岛市',
                '潮州市',
                '吉林市',
                '常德市',
                '宜春市',
                '黄冈市',
                '舟山市',
                '泰安市',
                '孝感市',
                '鄂尔多斯市',
                '开封市',
                '南平市',
                '齐齐哈尔市',
                '德州市',
                '宝鸡市',
                '马鞍山市',
                '郴州市',
                '安阳市',
                '龙岩市',
                '聊城市',
                '渭南市',
                '宿州市',
                '衢州市',
                '梅州市',
                '宣城市',
                '周口市',
                '丽水市',
                '安庆市',
                '三明市',
                '枣庄市',
                '南充市',
                '淮南市',
                '平顶山市',
                '东营市',
                '呼伦贝尔市',
                '乐山市',
                '张家口市',
                '清远市',
                '焦作市',
                '河源市',
                '运城市',
                '锦州市',
                '赤峰市',
                '六安市',
                '盘锦市',
                '宜宾市',
                '榆林市',
                '日照市',
                '晋中市',
                '怀化市',
                '承德市',
                '遂宁市',
                '毕节市',
                '佳木斯市',
                '滨州市',
                '益阳市',
                '汕尾市',
                '邵阳市',
                '玉林市',
                '衡水市',
                '韶关市',
                '吉安市',
                '北海市',
                '茂名市',
                '延边朝鲜族自治州',
                '黄山市',
                '阳江市',
                '抚州市',
                '娄底市',
                '营口市',
                '牡丹江市',
                '大理白族自治州',
                '咸宁市',
                '黔东南苗族侗族自治州',
                '安顺市',
                '黔南布依族苗族自治州',
                '泸州市',
                '玉溪市',
                '通辽市',
                '丹东市',
                '临汾市',
                '眉山市',
                '十堰市',
                '黄石市',
                '濮阳市',
                '亳州市',
                '抚顺市',
                '永州市',
                '丽江市',
                '漯河市',
                '铜仁市',
                '大同市',
                '松原市',
                '通化市',
                '红河哈尼族彝族自治州',
                '内江市',
                '长治市',
                '荆门市',
                '梧州市',
                '拉萨市',
                '汉中市',
                '四平市',
                '鹰潭市',
                '广元市',
                '云浮市',
                '葫芦岛市',
                '本溪市',
                '景德镇市',
                '六盘水市',
                '达州市',
                '铁岭市',
                '钦州市',
                '广安市',
                '保山市',
                '自贡市',
                '辽阳市',
                '百色市',
                '乌兰察布市',
                '普洱市',
                '黔西南布依族苗族自治州',
                '贵港市',
                '萍乡市',
                '酒泉市',
                '忻州市',
                '天水市',
                '防城港市',
                '鄂州市',
                '锡林郭勒盟',
                '白山市',
                '黑河市',
                '克拉玛依市',
                '临沧市',
                '三门峡市',
                '伊春市',
                '鹤壁市',
                '随州市',
                '新余市',
                '晋城市',
                '文山壮族苗族自治州',
                '巴彦淖尔市',
                '河池市',
                '凉山彝族自治州',
                '乌海市',
                '楚雄彝族自治州',
                '恩施土家族苗族自治州',
                '吕梁市',
                '池州市',
                '西双版纳傣族自治州',
                '延安市',
                '雅安市',
                '巴中市',
                '双鸭山市',
                '攀枝花市',
                '阜新市',
                '兴安盟',
                '张家界市',
                '昭通市',
                '海东市',
                '安康市',
                '白城市',
                '朝阳市',
                '绥化市',
                '淮北市',
                '辽源市',
                '定西市',
                '吴忠市',
                '鸡西市',
                '张掖市',
                '鹤岗市',
                '崇左市',
                '湘西土家族苗族自治州',
                '林芝市',
                '来宾市',
                '贺州市',
                '德宏傣族景颇族自治州',
                '资阳市',
                '阳泉市',
                '商洛市',
                '陇南市',
                '平凉市',
                '庆阳市',
                '甘孜藏族自治州',
                '大兴安岭地区',
                '迪庆藏族自治州',
                '阿坝藏族羌族自治州',
                '伊犁哈萨克自治州',
                '中卫市',
                '朔州市',
                '儋州市',
                '铜川市',
                '白银市',
                '石嘴山市',
                '莱芜市',
                '武威市',
                '固原市',
                '昌吉回族自治州',
                '巴音郭楞蒙古自治州',
                '嘉峪关市',
                '阿拉善盟',
                '阿勒泰地区',
                '七台河市',
                '海西蒙古族藏族自治州',
                '塔城地区',
                '日喀则市',
                '昌都市',
                '海南藏族自治州',
                '金昌市',
                '哈密市',
                '怒江傈僳族自治州',
                '吐鲁番市',
                '那曲地区',
                '阿里地区',
                '喀什地区',
                '阿克苏地区',
                '甘南藏族自治州',
                '海北藏族自治州',
                '山南市',
                '临夏回族自治州',
                '博尔塔拉蒙古自治州',
                '玉树藏族自治州',
                '黄南藏族自治州',
                '和田地区',
                '三沙市',
                '克孜勒苏柯尔克孜自治州',
                '果洛藏族自治州',
                ]
    for c in all_city:
        print(c, get_url_by_name(c + '环保局'))
