import time

def timestamp(func):

    def inner1():
        print(time.ctime())
        func()
    return inner1

