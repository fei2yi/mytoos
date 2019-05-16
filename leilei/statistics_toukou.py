import xlrd
dict ={}
gentype = ''
number = []
beizhu = {}
data = []
ll =0
ExcelFile = xlrd.open_workbook(r'Report_Haplotype_GT.2.xls', formatting_info=1)
sheet = ExcelFile.sheet_by_name('Sheet1')
num = []
mynum = []
col_index = []
mf_list = []
lie = {}
bianhao = []
margin = []
amend = {}
base_ = []
genum = []
getk = []
tkv = []
name = []
name1 = []
for row in range(0, sheet.nrows):
    rows = sheet.row_values(row)
    if row == 0:
        for col in range(0, sheet.ncols):
            name.append(rows[col])
    elif row == 1:
        for col in range(3, sheet.ncols):
            if rows[col] != ''  :
                num.append(int(rows[col]))
                mynum.append(int(rows[col]))
            elif rows[col] == '':
                num.append(num[-1])
        pre = ''
        lis_ind = []
        print('num',num)
        for i, vvv in enumerate(num):
            if i <=3  and vvv > 2:
                continue
            elif vvv == 2 or vvv == 1:
                continue
            elif vvv != pre:
                lis_ind = []
                lis_ind.append(i + 3)
                col_index.append(lis_ind)
            else:
                lis_ind.append(i + 3)
            pre = vvv
        temp = []
        print('col_index1',col_index)
        for clid, cl in enumerate(col_index):
            if clid == len(col_index) - 1:
                temp.append(cl)
            else:
                temp.append(cl[:-1])
                margin.append(cl[-2])
                amend [cl[-2]] = mynum[clid]
        col_index = temp
        print(col_index)
    elif row == 2:
        gx = rows
        print('rows',rows)
        MF_ = []
        for i, vvv in enumerate(rows):
            if vvv:
                MF_.append(vvv[0])
            elif not vvv and MF_:
                mf_list.append(MF_)
                MF_ = []
            if i == len(rows) - 1:
                mf_list.append(MF_)
        print('mf_list',mf_list)
# print('col_index',col_index)
    else:
        rews_h = []
        for h, vh in enumerate(rows):
            # print('vh',vh)
            # print('rows',rows)
            xfx = sheet.cell_xf_index(row, h)

            xf = ExcelFile.xf_list[xfx]
            print('xf',type(xf))
            bgx = xf.background.pattern_colour_index
            if bgx == 10 :
                rews_h.append(1)
            elif vh == '?':
                rews_h.append(2)
            else:
                rews_h.append(0)
        base_.append(rews_h)
# print('base',base_)
# print('mf_list',mf_list)
# print('col_index',col_index)
# print('margin',margin)
# print('name',name)
jsq = 0
js  = 0
blank = []
for row in range(1, sheet.nrows):
    rows = sheet.row_values(row)
    if row == 2 :
        for i ,mm in enumerate(margin):
            if rows[mm] == ''and rows[mm+1] == '' :
                blank.append(margin[i]-1)
            else :
                continue
for mfid, mf in enumerate(col_index):
    colid = col_index[mfid]
    if len(mf) == 2:
        jsp = 0
        for baseid, base in enumerate(base_):
            if base[colid[0]] ==2  and base[colid[1]] == 2:
                continue
            else:
                jsp += 1
        genum.append(jsp)
        znum = 0
        for ffid, id in enumerate(colid):
            for baseid, base in enumerate(base_):
                if base[id] == 1:
                    znum += 1
        if name[colid[0]] != '':
            name1.append(name[colid[0]])
        getk.append(znum)
        rag = (znum / jsp) * 100
        rag =( '%.2f' % rag) + '%'
        tkv.append(rag)
    elif len(mf) == 3:
        jsp1 = 0
        for baseid, base in enumerate(base_):
            if base[colid[0]] ==2  and base[colid[1]] == 2 and base[colid[2]] == 2:
                continue
            else:
                jsp1 += 1
        genum.append(jsp1)
        znum1 = 0
        for ffid, id in enumerate(colid):

            for baseid, base in enumerate(base_):
                if base[id] == 1:
                    znum1 += 1
        if name[colid] != '':
            name1.append(name[colid[0]])
        getk.append(znum1)
        rag = (znum1 / jsp1) * 100
        rag = ('%.2f' % rag) + '%'
        tkv.append(rag)
    elif len(mf) == 4 :
        jsp2 = 0
        for baseid, base in enumerate(base_):
            if base[colid[0]] ==2  and base[colid[1]] == 2 and base[colid[2]] == 2 and base[colid[2]]:
                continue
            else:
                jsp2 += 1
        genum.append(jsp2)
        znum2 = 0
        for ffid, id in enumerate(colid):
            for baseid, base in enumerate(base_):
                if base[id] == 1:
                    znum2 += 1
        if name[colid] != '':
            name1.append(name[colid[0]])
        getk.append(znum2)
        rag = (znum2 / jsp2) * 100
        rag = ('%.2f' % rag) + '%'
        tkv.append(rag)
    elif len(mf) == 1 :
        jsp3 = 0
        for baseid, base in enumerate(base_):
            if base[colid[0]] ==2 :
                continue
            else:
                jsp3 += 1
        genum.append(jsp3)
        znum3 = 0
        for ffid, id in enumerate(colid):
            if len(colid) == 2:
                continue
            else:
                for baseid, base in enumerate(base_):
                    if base[id] == 1:
                        znum3 += 1
                if name[colid[0]] != '':
                    name1.append(name[colid[0]])
        getk.append(znum3)
        rag = (znum3 / jsp3) * 100
        rag = ('%.2f' % rag) + '%'
        tkv.append(rag)
# print('name1',name1)
# print('genum',genum)
# print('getk',getk)
# print('tkv',tkv)
item0 = ['姓名','总数','脱扣数','脱口率']
with open('Report_trip.txt', 'w') as f:
    f.write('	'.join(item0) + '\n')
    for i in range(len(name1)):
        new_lis = [name1[i],genum[i],getk[i],tkv[i]]
        new_lis = [str(iii) for iii in new_lis]
        f.write('	'.join(new_lis) + '\n')
    f.close()