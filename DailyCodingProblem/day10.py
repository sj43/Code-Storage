import time
import threading


class Scheduler:
    def __init__(self):
        pass

    def delay(self, f, n):
        def sleep_then_call():
            time.sleep(n / 1000)
            f()
        t = threading.Thread(target=sleep_then_call)
        t.start()


def function1():
    print("threading complete")


scheduler = Scheduler()
scheduler.delay(function1, 2000)
