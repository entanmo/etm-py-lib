# -*- encoding: utf-8 -*-
from binascii import hexlify, unhexlify


class Delegate:
    @staticmethod
    def create(data, tr):
        tr["recipientId"] = "A4MFB3MaPd355ug19GYPMSakCAWKbLjDTb"  # TODO: 零时添加以后换成基金会地址
        tr["amount"] = 1000 * 100000000
        tr["asset"]["delegate"] = {
            "username": data["username"].lower().replace(' ', ''),
            "publicKey": str(hexlify(data["sender"]["publicKey"].to_bytes()), encoding="utf-8")
        }

        # if tr["asset"]["delegate"]["username"]:
        #     tr["asset"]["delegate"]["username"] = tr["asset"]["delegate"]["username"].toLowerCase().trim()

        return tr

    @staticmethod
    def getBytes(tr):
        if not tr["asset"]["delegate"]["username"]:
            return None

        buf = bytes()
        try:
            buf = bytes(tr["asset"]["delegate"]["username"], "utf-8")
        except:
            raise

        return buf
