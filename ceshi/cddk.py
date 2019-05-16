from gpcharts import figure
import random
#
my_fig = figure()
my_fig.title = 'Random Histrogram'
my_fig.xlabel = 'Random Values'
vals = [10, 40, 30, 50, 80, 100]
my_fig.hist(vals)