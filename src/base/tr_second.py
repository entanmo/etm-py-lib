# -*- encoding: utf-8 -*-
from binascii import hexlify, unhexlify


class Second:
    @staticmethod
    def create(data, tr):
        tr["asset"]["signature"] = {
            "publicKey": str(hexlify(data["secondKeypair"]["publicKey"].to_bytes()), encoding="utf-8")
        }
        return tr

    @staticmethod
    def getBytes(tr):
        if not tr["asset"]["signature"]["publicKey"]:
            return None

        buf = bytes()
        try:
            buf = bytes(tr["asset"]["signature"]["publicKey"], "utf-8")
        except:
            raise

        return buf
