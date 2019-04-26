import hashlib
from binascii import hexlify, unhexlify
import base58

NORMAL_PREFIX = 'A'


class Address:
    def isAddress(self, address):
        return self.isBase58CheckAddress(address)

    def isBase58CheckAddress(self, address):
        if not isinstance(address, str):
            return False

        if address[0] != 'A':
            return False

        try:
            base58.b58decode_check(address[1:])
        except ValueError:
            return False

        return True

    @staticmethod
    def generateBase58CheckAddress(publicKey):
        if isinstance(publicKey, str):
            publicKey = unhexlify(publicKey)

        hash = hashlib.sha256(publicKey).digest()
        ripemd = hashlib.new('ripemd160', hash).digest()

        return NORMAL_PREFIX + str(base58.b58encode_check(ripemd), encoding="utf-8")
