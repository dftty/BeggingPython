"""
类
"""

from time import sleep

class Clock:

    def __init__(self, hour, minute, seconds):
        self.hour = hour
        self.minute = minute
        self.seconds = seconds

    def run(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0

    def show(self):
        print("现在时间是：%02d:%02d:%02d" % (self.hour, self.minute, self.seconds))

def main():
    c = Clock(0, 0, 0)
    while True:
        c.run()
        c.show()
        sleep(0.1)


if __name__ == "__main__":
    main()