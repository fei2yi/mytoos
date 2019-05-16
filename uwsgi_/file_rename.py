import os

aaa = {
    '1000': 'VXM6P',
    '1001': 'Q548U',
    '1002': 'BQD4P',
    '1003': 'MVNNH',
    '1004': '8NSPN',
    '1005': 'QWRQR',
    '1006': 'FYQGL',
    '1007': 'DJDCG',
    '1008': 'RW29Q',
    '1009': 'DS5N2',
    '1010': '8H574',
    '1011': '5AKNN',
    '1012': 'LSFCL',
    '1013': 'UXXGZ',
    '1014': 'WD344',
    '1015': 'RHPVV',
    '1016': 'Z96SV',
    '1017': 'W6MAW',
    '1018': '7FSM5',
    '1019': '7PHVM',
    '1020': 'S4NSB',
    '1021': 'UXR4D',
    '1022': 'HJGLL',
    '1023': 'MSABN',
    '1024': 'EEFKF',
    '1025': 'FASBE',
    '1026': 'APXTW',
    '1027': 'EWDAK',
    '1028': 'XRABY',
    '1029': 'JYU22',
    '1030': '67X4T',
    '1031': 'TZAPK',
    '1032': 'YANU6',
    '1033': 'VGTP4',
    '1034': 'MY3P9',
    '1035': 'SEG8W',
    '1036': '862WT',
    '1037': '6TZWG',
    '1038': '7ZFE7',
    '1039': 'HRJBV',
    '103': 'BKK9H',
    '1040': 'KYCAX',
    '1041': 'G9HBL',
    '1042': 'XR9PX',
    '1043': '8TZXU',
    '1044': 'JT9QS',
    '1045': 'Z3MCW',
    '1046': 'ZH87L',
    '1047': 'JHRPL',
    '1048': 'EUS9B',
    '1049': 'HBRVZ',
    '104': 'ZAP4M',
    '1050': 'QNNUQ',
    '1051': 'JN84Q',
    '1052': 'C2HSR',
    '1053': 'W49W7',
    '1054': 'NUZHW',
    '1055': '55U38',
    '1056': 'QWUPQ',
    '1057': 'ST3FE',
    '1058': '8J3D5',
    '1059': 'DBPUE',
    '105': 'QXNUP',
    '1060': 'WXYNU',
    '1061': '2X436',
    '1062': 'TSNUC',
    '1063': 'BN6CT',
    '1064': '3Z9Y2',
    '1065': 'WVZ6G',
    '1066': 'F79ZQ',
    '1067': 'FBKVS',
    '1068': 'ZGAF4',
    '1069': 'ZPTN5',
    '106': '9KMML',
    '1070': 'BVBUX',
    '1071': 'MFH72',
    '1072': 'S77SB',
    '1073': 'LFQ3E',
    '1074': '6URSF',
    '1075': 'UTQK2',
    '1076': '8R7T2',
    '1077': '84TDN',
    '1078': '7ZPMQ',
    '1079': 'YHKDT',
    '107': 'W2MV3',
    '1080': '4J6N9',
    '1081': '9XW6K',
    '1082': 'ZWDY8',
    '1083': '4G2CF',
    '1084': '894NS',
    '1085': 'D4AB4',
    '1086': 'LEHB5',
    '1087': 'E9EJG',
    '1088': 'YN5AJ',
    '1089': 'KY9JX',
    '108': '34LPL',
    '1090': 'K4G46',
    '1091': 'NTM8W',
    '1092': 'Z9EKN',
    '1093': 'VFCLN',
    '1094': 'R2KCY',
    '1095': '59GFC',
    '1096': 'E6E93',
    '1097': '834A9',
    '1098': 'V72VA',
    '1099': 'YGDHW',
    '109': 'BP53T',
    '1100': 'ZMTFS',
    '1101': 'KPDS2',
    '1102': '3EUXS',
    '1103': '3C458',
    '1104': 'G58YE',
    '1105': '98B6S',
    '1106': 'A4P6Q',
    '1107': '8T92E',
    '1108': 'PSUFQ',
    '1109': 'X59PG',
    '110': 'YPBTA',
    '1110': 'RM989',
    '1111': 'ECR5F',
    '1112': 'EMGCB',
    '1113': 'KS8T7',
    '1114': 'CA4HU',
    '1115': 'BCG75',
    '1116': 'WQJGK',
    '1117': 'KV54Y',
    '1118': 'P743Y',
    '1119': '8UM8S',
    '111': '6JHEZ',
    '1120': '52X84',
    '1121': 'A8NVC',
    '1122': 'NR8CU',
    '1123': '3NMPK',
    '1124': '5JXHD',
    '1125': 'QXB66',
    '1126': '9ZVMK',
    '1127': 'J4GV9',
    '1128': 'CJ5K7',
    '1129': '7GA87',
    '112': '6FVPN',
    '1130': 'HEPVA',
    '1131': 'TELHE',
    '1132': '763AY',
    '1133': 'HMRCR',
    '1134': '7HVFY',
    '1135': 'TKPHL',
    '1136': 'RGGBH',
    '1137': 'YYUHU',
    '1138': '9LTHH',
    '1139': 'RVDMY',
    '113': '5MC58',
    '1140': 'AH58R',
    '1141': 'Q7VZM',
    '1142': 'JDHTV',
    '1143': 'B27DN',
    '1144': '2FF8R',
    '1145': '3T8XV',
    '1146': 'Q4TN9',
    '1147': '8NA7S',
}


def get_newname(oldname):
    key = oldname.split('_')[-1].split('.')[0]
    value = aaa.get(key)
    if key in aaa.keys():
        newname = 'E:\data\zqsx2\\' + value.lower() + '_' + key + '.' + 'png'
        return newname
    else:
        return None


path = 'E:\data\zqsx\\'
f = os.listdir(path)
for n, i in enumerate(f):
    oldname = path + f[n]
    newname = get_newname(oldname)
    if newname:
        os.rename(oldname, newname)
        print(oldname, '======>', newname)
