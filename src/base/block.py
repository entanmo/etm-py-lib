# -*- encoding: utf-8 -*-

import hashlib
from binascii import hexlify, unhexlify

from src.utils.ed import Ed
from src.utils.buffer import BytesBuffer

from src.base.transaction import Transaction

ed = Ed()
transactionModule = Transaction()


class Block:

    def create(self, data):

        block = {

        }
        return block

    def getBytes(self, block):
        size = 4 + 4 + 64 + 4 + 8 + 8 + 8 + 4 + 32 + 32 + 64
        _bytes = bytes()
        try:
            bb = BytesBuffer(size, True)
            bb.writeInt(block["version"])
            bb.writeInt(block["timestamp"])

            if "previousBlock" in block:
                bb.writeString(block["previousBlock"])
            else:
                bb.writeString('0')

            bb.writeInt(block["numberOfTransactions"])
            bb.writeLong(block["totalAmount"])
            bb.writeLong(block["totalFee"])
            bb.writeLong(block["reward"])

            bb.writeInt(block["payloadLength"])

            payloadHash_buffer = unhexlify(block["payloadHash"])
            bb.writeString(payloadHash_buffer)

            generatorPublicKey_buffer = unhexlify(block["generatorPublicKey"])
            bb.writeString(generatorPublicKey_buffer)

            if "blockSignature" in block:
                blockSignature_buffer = unhexlify(block["blockSignature"])
                bb.writeString(blockSignature_buffer)

            _bytes = bb.tobytes()

        except:
            raise

        return _bytes

    def getHash(self, block):
        _bytes = self.getBytes(block)
        return hashlib.sha256(_bytes).digest()

    def getId(self, block):
        _hash = self.getHash(block)
        return str(hexlify(_hash), encoding="utf-8")

    def getSignature(self, block, keypair):
        _hash = self.getHash(block)
        _sign = ed.Sign(_hash, keypair)
        return str(hexlify(_sign), encoding="utf-8")
