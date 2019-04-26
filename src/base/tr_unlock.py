class Unlock:
    @staticmethod
    def create(data, tr):
        tr["args"] = data["args"]
        return tr

    @staticmethod
    def getBytes(tr):
        return None
