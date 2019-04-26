class Lock:
    @staticmethod
    def create(data, tr):
        tr["asset"]["lock"] = {
            "locks": data["locks"]
        }
        return tr

    @staticmethod
    def getBytes(tr):
        if not tr["asset"]["lock"]["locks"]:
            return None

        buf = bytes()
        try:
            buf = bytes(tr["asset"]["lock"]["locks"], "utf-8")
        except:
            raise

        return buf
