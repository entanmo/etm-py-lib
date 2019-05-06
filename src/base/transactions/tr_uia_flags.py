# -*- encoding: utf-8 -*-
from src.utils.buffer import BytesBuffer

class UiaFlags:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = ""
        tr["amount"] = 0
        tr["asset"]["uiaFlags"] = {
            "currency": data["currency"],
            "flagType": data["flagType"],
            "flag": data["flag"]
        }
        return tr

    @staticmethod
    def getBytes(tr):
        uiaFlags = tr["asset"]["uiaFlags"]
        bb = BytesBuffer(256)
        bb.writeString(uiaFlags["currency"])
        bb.writeByte(uiaFlags["flagType"])
        bb.writeByte(uiaFlags["flag"])

        return bb.tobytes()
