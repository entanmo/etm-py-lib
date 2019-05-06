# -*- encoding: utf-8 -*-

class UiaTransfer:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = data["recipientId"]
        tr["amount"] = 0
        tr["asset"]["uiaTransfer"] = {
            "currency": data["currency"],
            "amount": data["amount"]
        }
        return tr

    @staticmethod
    def getBytes(tr):
        buf = bytes()
        try:
            buf1 = bytes("".join(tr["asset"]["uiaTransfer"]["currency"]), "utf-8")
            buf2 = bytes("".join(tr["asset"]["uiaTransfer"]["amount"]), "utf-8")
            buf = buf1 + buf2
        except:
            raise

        return buf
