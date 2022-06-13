import time


class Test:
    def __init__(self):
        pass

    def time(self, func, param):
        start = time.time()
        rVal = func(param)
        end = time.time()
        return('Function took ' + str(((end - start)*1000))+'ms ' + 'to execute with the following return value: ' + str(rVal))
