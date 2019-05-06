# -*- encoding: utf-8 -*-
from binascii import hexlify, unhexlify
class UiaIssuer:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = ""
        tr["amount"] = 0
        tr["asset"]["uiaIssuer"] = {
            "name": data["name"],
            "desc": data["desc"]
        }
        return tr

    @staticmethod
    def getBytes(tr):
        buf = bytes()
        try:
            buf1 = bytes("".join(tr["asset"]["uiaIssuer"]["name"]), "utf-8")
            buf2 = bytes("".join(tr["asset"]["uiaIssuer"]["desc"]), "utf-8")
            buf = buf1 + buf2
        except:
            raise

        return buf
