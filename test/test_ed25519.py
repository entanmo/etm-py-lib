import ed25519, ed25519sha3, ed25519_blake2b
import hashlib

# "publicKey ": "07187396934e832fc08c8ec0f3095d6c7cce3eb2c53568f0bbafebb3ffa7c582",
# "privateKey": "f85a3d9142d4d6a7a0ce437f46a9a373f5ae6c663d1842676a8218d8ab8ff63e07187396934e832fc08c8ec0f3095d6c7cce3eb2c53568f0bbafebb3ffa7c582",

hash = hashlib.sha256(b'real rally sketch sorry place parrot typical cart stone mystery age nominee')


'''类中调用'''
class EEE:
    def keypair(self, hash):
        sk = ed25519.SigningKey(hash)
        return sk


ed = EEE()
sk = ed.keypair(hash.digest())
print(sk.to_ascii(encoding="hex"))

'''方法调用'''
# def keypair(hash):
#     sk = ed25519.SigningKey(hash)
#     return sk
#
#
# keypair(hash.digest())

'''直接调用'''
# sk = ed25519.SigningKey(hash.digest())
# print(sk.to_ascii(encoding="hex"))


'''ed25519 vs ed25519sha3 vs ed25519_blake2b'''

# sk1 = ed25519.SigningKey(hash.digest())
# vk1 = sk1.get_verifying_key()
# print("ed25519        :",sk1.to_ascii(encoding="hex"))
# print("ed25519        :",vk1.to_ascii(encoding="hex"))
#
# sk1 = ed25519sha3.SigningKey(hash.digest())
# vk1 = sk1.get_verifying_key()
# print("ed25519sha3    :",sk1.to_ascii(encoding="hex"))
# print("ed25519sha3    :",vk1.to_ascii(encoding="hex"))
#
# sk2 = ed25519_blake2b.SigningKey(hash.digest())
# vk2 = sk2.get_verifying_key()
# print("ed25519_blake2b:",sk2.to_ascii(encoding="hex"))
# print("ed25519_blake2b:",vk2.to_ascii(encoding="hex"))
