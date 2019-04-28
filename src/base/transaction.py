# -*- encoding: utf-8 -*-

import hashlib
from binascii import hexlify, unhexlify

from src.base.tr_transfer import Transfer
from src.base.tr_delegate import Delegate
from src.base.tr_undelegate import Undelegate
from src.base.tr_lock import Lock
from src.base.tr_unlock import Unlock
from src.base.tr_vote import Vote
from src.base.tr_delay import Delay
from src.base.tr_second import Second

from src.utils.ed import Ed
from src.utils.slots import Slots
from src.utils.buffer import BytesBuffer

ed = Ed()
slots = Slots()


class Transaction:
    o_trsTypes = {
        0: Transfer(),
        2: Delegate(),
        120: Undelegate(),
        101: Lock(),
        102: Unlock(),
        3: Vote(),
        110: Delay(),
        1: Second()
    }

    def create(self, data):
        if "type" not in data or data["type"] not in self.o_trsTypes:
            raise Exception('Unknown transaction type ' + data["type"])

        if "sender" not in data:
            raise Exception("Can't find sender")

        if "keypair" not in data:
            raise Exception("Can't find keypair")

        _senderPublicKey = None
        if "publicKey" in data["sender"]:
            _senderPublicKey = str(hexlify(data["sender"]["publicKey"].to_bytes()), encoding="utf-8")

        tr = {
            "type": data["type"],
            "amount": 0,
            "fee": data["fee"] if "fee" in data else 0,
            "timestamp": slots.getTime(),
            "senderPublicKey": _senderPublicKey,
            "asset": {},
            "args": data["args"] if "args" in data else [],
            "message": data["message"] if "message" in data else ""
        }

        tr = self.o_trsTypes[tr["type"]].create(data, tr)

        tr["signature"] = self.getSignature(tr, data["keypair"])

        if tr["type"] != 1 and "secondKeypair" in data:
            tr["signSignature"] = self.getSignature(tr, data["secondKeypair"])

        tr["id"] = self.getId(tr)

        return tr

    def getBytes(self, tr, skipSignature, skipSecondSignature):
        if tr["type"] not in self.o_trsTypes:
            raise Exception('Unknown transaction type ' + tr["type"])

        size = 1 + 4 + 32 + 32 + 8 + 8 + 64 + 64
        _bytes = bytes()

        try:
            assetBytes = self.o_trsTypes[tr["type"]].getBytes(tr)
            assetSize = len(assetBytes) if assetBytes else 0
            # assetSize = 0

            bb = BytesBuffer(size + assetSize, True)

            bb.writeByte(tr["type"])

            bb.writeInt(tr["timestamp"])

            senderPublicKey_buffer = unhexlify(tr["senderPublicKey"])
            # bb.writeString(senderPublicKey_buffer)
            for i in iter(senderPublicKey_buffer):
                bb.writeByte(i)

            if "requesterPublicKey" in tr:
                requesterPublicKey_buffer = unhexlify(tr["requesterPublicKey"])
                for i in iter(requesterPublicKey_buffer):
                    bb.writeByte(i)

            if "recipientId" in tr:
                bb.writeString(tr["recipientId"])
            else:
                for i in range(8):
                    bb.writeByte(0)

            bb.writeLong(tr["amount"])

            if tr["message"]:
                bb.writeString(tr["message"])

            if tr["args"]:
                for i in tr["args"]:
                    bb.writeString(i)

            if assetSize > 0:
                print(assetBytes)
                for i in iter(assetBytes):
                    bb.writeByte(i)

            if not skipSignature and "signature" in tr:
                signature_buffer = unhexlify(tr["signature"])
                for i in iter(signature_buffer):
                    bb.writeByte(i)

            if not skipSecondSignature and "signSignature" in tr:
                signSignature_buffer = unhexlify(tr["signSignature"])
                for i in iter(signSignature_buffer):
                    bb.writeByte(i)

            _bytes = bb.tobytes()

        except:
            raise

        return _bytes

    def getHash(self, tr):
        _bytes = self.getBytes(tr, False, False)
        return hashlib.sha256(_bytes).digest()

    def getId(self, tr):
        _hash = self.getHash(tr)
        return str(hexlify(_hash), encoding="utf-8")

    def getSignature(self, tr, keypair):
        _hash = self.getHash(tr)
        _sign = ed.Sign(_hash, keypair)
        return str(hexlify(_sign), encoding="utf-8")

    def getMultiSignature(self, tr, keypair):
        _bytes = self.getBytes(tr, True, True)
        _hash = hashlib.sha256(_bytes).digest()
        _sign = ed.Sign(_hash, keypair)
        return str(hexlify(_sign), encoding="utf-8")
