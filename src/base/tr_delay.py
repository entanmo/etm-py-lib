class Delay:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = data["recipientId"]
        tr["amount"] = data["amount"]
        tr["args"] = data["args"]
        return tr

    @staticmethod
    def getBytes(tr):
        return None
