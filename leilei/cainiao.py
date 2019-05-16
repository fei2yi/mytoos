import xlrd
from win32com import client as wc
from docx import Document
kinship,amend = {},{}
name,num,mynum,col_index,margin,mf_list,ROW = [],[],[],[],[],[],[]
# def doSaveAas():
# word = wc.Dispatch('Word.Application')
# doc = word.Documents.Open(u'aaaa.doc')  # 目标路径下的文件
# doc.SaveAs(u'E:\\bin\\tuokoulv\\aaaa.docx', 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
# doc.Close()
# word.Quit()
path = 'aaaa.docx'
document = Document(path) #读入文件
tables = document.tables #获取文件中的表格集
table1 = tables[2]
for row in range(1,len(table1.rows)):
    kinship[table1.cell(row,0).text] = table1.cell(row,2).text
print('kinship',kinship)
table = tables[-2 ]#获取文件中的第一个表格
for row in range(0,len(table.rows)):#从表格第二行开始循环读取表格数据
    if row == 0:
        for col in range(0, len(table.columns)):
            name.append(table.cell(row,col).text)
        for col in range(3, len(table.columns)):
            if table.cell(row,col).text != '':
                num.append(table.cell(row,col).text)
                mynum.append(table.cell(row,col).text)
            elif table.cell(row,col).text == '':
                num.append(num[-1])
        pre = ''
        lis_ind = []
        print('num',num)
        for i, vvv in enumerate(num):
            if kinship[vvv] != '胚胎':
                continue
            elif vvv != pre:
                lis_ind = []
                lis_ind.append(i + 3)
                col_index.append(lis_ind)
            else:
                lis_ind.append(i + 3)
            pre = vvv
        temp = []
        # print('col_index1',col_index)
        for clid, cl in enumerate(col_index):
            if clid == len(col_index) - 1:
                temp.append(cl)
            else:
                temp.append(cl[:-1])
                margin.append(cl[-2])
                amend [cl[-2]] = mynum[clid]
        col_index = temp
        print('col_index',col_index)
    #cell(i,0)表示第(i+1)行第1列数据，以此类推
    elif row == 1:
        for col in range(0, len(table.columns)):
            if col < 3:
                ROW.append('')
            else:
                ROW.append(table.cell(row,col).text)
        print('ROW', ROW)
        MF_ = []
        for i, vvv in enumerate(ROW):
            if vvv:
                MF_.append(vvv[0])
            elif not vvv and MF_:
                mf_list.append(MF_)
                MF_ = []
            if i == len(ROW) - 1:
                mf_list.append(MF_)
        print('mf_list',mf_list)
    else:
        rews_h = []
        xf = []
        for h, vh in enumerate(ROW):
            # print('vh',vh)
            # print('rows',rows)
            xf = table.cell(row,h)
            print(type(xf))
            print(xf.background)

            # bgx = xfx.background.pattern_colour_index
            # if bgx == 10:
            #     rews_h.append(1)
            # elif vh == '?':
            #     rews_h.append(2)
            # else:
            #     rews_h.append(0)
        # base_.append(rews_h)
# doSaveAas()
