# -*- encoding: utf-8 -*-
import struct


class UiaAsset:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = ""
        tr["amount"] = 0
        tr["asset"]["uiaAsset"] = {
            "name": data["name"],
            "desc": data["desc"],
            "maximum": data["maximum"],
            "precision": data["precision"],
            "strategy": data["strategy"],
            "allowWriteoff": data["allowWriteoff"],
            "allowWhitelist": data["allowWhitelist"],
            "allowBlacklist": data["allowBlacklist"]
        }
        return tr

    @staticmethod
    def getBytes(tr):
        uiaAsset = tr["asset"]["uiaAsset"]
        buf = bytes()
        try:
            buf1 = bytes("".join(uiaAsset["name"]), "utf-8")
            buf2 = bytes("".join(uiaAsset["desc"]), "utf-8")
            buf3 = bytes("".join(uiaAsset["maximum"]), "utf-8")
            buf4 = bytes(struct.pack("<I", (uiaAsset["precision"] if uiaAsset["precision"] else 0))[:1])
            buf5 = bytes("".join(uiaAsset["strategy"]), "utf-8")
            buf6 = bytes(struct.pack("<I", (uiaAsset["allowWriteoff"] if uiaAsset["allowWriteoff"] else 0))[:1])
            buf7 = bytes(struct.pack("<I", (uiaAsset["allowWhitelist"] if uiaAsset["allowWhitelist"] else 0))[:1])
            buf8 = bytes(struct.pack("<I", (uiaAsset["allowBlacklist"] if uiaAsset["allowBlacklist"] else 0))[:1])

            buf = buf1 + buf2 + buf3 + buf4 + buf5 + buf6 + buf7 + buf8
        except:
            raise

        return buf
