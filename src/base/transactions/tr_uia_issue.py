# -*- encoding: utf-8 -*-

class UiaIssue:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = ""
        tr["amount"] = 0
        tr["asset"]["uiaIssue"] = {
            "currency": data["currency"],
            "amount": data["amount"]
        }
        return tr

    @staticmethod
    def getBytes(tr):
        buf = bytes()
        try:
            buf1 = bytes("".join(tr["asset"]["uiaIssue"]["currency"]), "utf-8")
            buf2 = bytes("".join(tr["asset"]["uiaIssue"]["amount"]), "utf-8")
            buf = buf1 + buf2
        except:
            raise

        return buf
