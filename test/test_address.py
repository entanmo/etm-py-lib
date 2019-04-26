from src.utils.address import Address
import hashlib
import base58, base58check
from binascii import hexlify, unhexlify

NORMAL_PREFIX = 'A'
address = Address()


# A4rNr2VzCq2jnmhzxkvjY9PsPmhcmSEfiw
addr = address.generateBase58CheckAddress("07187396934e832fc08c8ec0f3095d6c7cce3eb2c53568f0bbafebb3ffa7c582")
print(addr)


def generateBase58CheckAddress(publicKey):
    print("publicKey", publicKey)
    if isinstance(publicKey, str):
        publicKey = unhexlify(publicKey)

    # hash = hashlib.sha256(publicKey)
    # hash = SHA256.new()
    # hash.update(publicKey)
    #
    # ripemd = RIPEMD.new()
    # ripemd.update(hash.digest())

    print("publicKey", hexlify(publicKey))
    hash = hashlib.sha256(publicKey).digest()
    print("h1", hexlify(hash))
    ripemd = hashlib.new('ripemd160', hash).digest()
    print("h2", hexlify(ripemd))
    # return NORMAL_PREFIX + str(base58check.b58encode(ripemd), encoding="utf-8")

    return NORMAL_PREFIX + str(base58.b58encode_check(ripemd), encoding="utf-8")


# addr0 = generateBase58CheckAddress("07187396934e832fc08c8ec0f3095d6c7cce3eb2c53568f0bbafebb3ffa7c582")
# print(addr0)
