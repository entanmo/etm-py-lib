# -*- encoding: utf-8 -*-

class Transfer:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = data["recipientId"]
        tr["amount"] = data["amount"]
        return tr

    @staticmethod
    def getBytes(tr):
        return None
