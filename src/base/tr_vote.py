from src.utils.buffer import BytesBuffer


class Vote:
    @staticmethod
    def create(data, tr):
        tr["asset"]["vote"] = {
            "votes": data["votes"]
        }

        return tr

    @staticmethod
    def getBytes(tr):
        if not tr["asset"]["vote"]["votes"]:
            return None

        buf = bytes()
        try:
            buf = bytes(tr["asset"]["vote"]["votes"], "utf-8")
        except:
            raise

        return buf
