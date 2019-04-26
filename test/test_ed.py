import hashlib
from src.utils.ed import Ed
from binascii import hexlify, unhexlify

ed = Ed()

hash = hashlib.sha256(b'real rally sketch sorry place parrot typical cart stone mystery age nominee').digest()
keypair = ed.MakeKeypair(hash)


def test_keypair():
    print(keypair['publicKey'].to_ascii(encoding="hex"))
    print(keypair['privateKey'].to_ascii(encoding="hex"))


def test_sign():
    h = hashlib.sha256(b'abc').digest()
    sign = ed.Sign(h, keypair)
    print(sign)
    hexSign = hexlify(sign)
    print(hexSign)
    originSign = unhexlify(hexSign)
    print(originSign)


def test_verify():
    h = hashlib.sha256(b'abc').digest()
    sign = ed.Sign(h, keypair)
    print(hexlify(sign))

    h2 = hashlib.sha256(b'abcd').digest()
    sign2 = ed.Sign(h2, keypair)

    v = ed.Verify(h2, sign2, keypair['publicKey'])
    print(v)



# test_keypair()
test_sign()
# test_verify()
