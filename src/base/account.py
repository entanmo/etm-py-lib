# -*- encoding: utf-8 -*-

import hashlib
from binascii import hexlify, unhexlify

from src.utils.ed import Ed
from src.utils.address import Address

ed = Ed()
address = Address()

class Account:
    def getKeypairBySecret(self, secret):
        hash = hashlib.sha256(bytes(secret, encoding="utf-8")).digest()
        keypair = ed.MakeKeypair(hash)

        return {
            "publicKey": str(keypair['publicKey'].to_ascii(encoding="hex"), encoding="utf-8"),
            "privateKey": str(keypair['privateKey'].to_ascii(encoding="hex"), encoding="utf-8")
        }

    def getAddressByPublicKey(self,publicKey):
        return address.generateBase58CheckAddress(publicKey)