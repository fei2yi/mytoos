def ff():
    raise Exception('1234')


while True:
    try:
        ff()
        break
    except TypeError:
        print("pika.exceptions.ConnectionClosed", time.ctime())
