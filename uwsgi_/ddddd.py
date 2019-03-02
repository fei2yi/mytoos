from gpcharts import figure
# 获取图像对象并设置x，y轴的值
fig3 = figure()
xVals = ['Temps','2016-03-20','2016-03-21','2016-03-25','2016-04-01']
yVals = [['Shakuras','Korhal','Aiur'],[10,30,40],[12,28,41],[15,34,38],[8,33,47]]
# 添加标题和Y轴标注，画条形图
fig3.title = 'Weather over Days'
fig3.ylabel = 'Dates'
fig3.bar(xVals, yVals)