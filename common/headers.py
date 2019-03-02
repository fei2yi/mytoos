# -*- coding: utf-8 -*-

st = '''
bmmc: DEPT_NJ_HUANBAO
sw: 
currPage: 2
pageSize: 10
'''
for i in st.split('\n'):
    if i:
        if i.startswith(':'):
            i = i[1:]
            i = i.replace(':', "':'", 1)
            i = ':' + i
        else:
            i = i.replace(':', "':'", 1).replace(' ','',1)
        i = "'" + i + "'" + ","

        print(i)
