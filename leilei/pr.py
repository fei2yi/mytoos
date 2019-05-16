ppp = """bianliang{} = int(rst[{}]['pid'])"""

for i in range(0, 100):
    ppp0 = ppp.format(i+1, i)
    print(ppp0)
