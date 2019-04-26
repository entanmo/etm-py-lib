import time
import datetime
import math


class Slots:
    interval = 3
    delegates = 101
    roundBlocks = 101 * 1
    leading = 7
    powTimeOut = 2

    @staticmethod
    def beginEpochTime():
        d = datetime.datetime(2018, 9 + 1, 12, 12 + 8, 0, 0, 0)
        return d

    def getTime(self, time=time.time()):
        d = self.beginEpochTime()
        return math.floor(time - d.timestamp())

    def getRealTime(self, *epochTime):
        if not epochTime:
            epochTime = self.getTime()

        d = self.beginEpochTime()
        t = math.floor(d.timestamp()) * 1000
        return t + epochTime * 1000

    def getSlotNumber(self, *epochTime):
        if not epochTime:
            epochTime = self.getTime()

        return math.floor(epochTime / self.interval)

    def getSlotTime(self, slot):
        return slot * self.interval

    def getNextSlot(self, slot):
        return self.getSlotNumber() + 1

    def getLastSlot(self, nextSlot):
        return nextSlot + self.delegates

    def roundTime(self, date):
        return math.floor(date.timestamp()) * 1000

    def getHeightPerDay(self, slot):
        return math.floor(24 * 60 * 60 / self.interval)
