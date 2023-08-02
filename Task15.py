import threading ,time
def lw():
    while True:
        print("aaaaaaaaaaa")
        time.sleep(1)
def b():
    while True:
        print("bbbbbbbbbbb")
        time.sleep(2)
h1=threading.Thread(target=lw)
h2=threading.Thread(target=b)
h1.start()
h2.start()