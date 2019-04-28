# -*- encoding: utf-8 -*-

class Undelegate:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = ""
        tr["amount"] = 0
        return tr

    @staticmethod
    def getBytes(tr):
        return None
