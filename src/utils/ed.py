# -*- encoding: utf-8 -*-

import ed25519


class Ed:
    @staticmethod
    def MakeKeypair(hash):
        sk = ed25519.SigningKey(hash)
        vk = sk.get_verifying_key()

        return {
            "publicKey": vk,
            "privateKey": sk
        }

    @staticmethod
    def Sign(hash, keypair):
        sign = keypair["privateKey"].sign(hash)
        return sign

    @staticmethod
    def Verify(hash, sign, publicKey):
        try:
            publicKey.verify(sign, hash)
        except ed25519.BadSignatureError:
            return False
        else:
            return True
