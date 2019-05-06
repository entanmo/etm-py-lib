# -*- encoding: utf-8 -*-
from src.utils.buffer import BytesBuffer


class UiaAcl:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = ""
        tr["amount"] = 0
        tr["asset"]["uiaAcl"] = {
            "currency": data["currency"],
            "operator": data["operator"],
            "flag": data["flag"],
            "list": data["list"]
        }
        return tr

    @staticmethod
    def getBytes(tr):
        uiaAcl = tr["asset"]["uiaAcl"]
        bb = BytesBuffer(256)
        bb.writeString(uiaAcl["currency"])
        bb.writeString(uiaAcl["operator"])
        bb.writeByte(uiaAcl["flag"])
        for i in uiaAcl["list"]:
            bb.writeString(i)

        return bb.tobytes()
