
import hashlib
from binascii import hexlify, unhexlify

from src.base.transaction import Transaction
from src.utils.ed import Ed

tr = Transaction()
ed = Ed()

secret = "race forget pause shoe trick first abuse insane hope budget river enough"
hash = hashlib.sha256(bytes(secret,encoding="utf-8")).digest()
# print(hexlify(hash))

keypair = ed.MakeKeypair(hash)
# print(keypair['publicKey'].to_ascii(encoding="hex"))
# print(keypair['privateKey'].to_ascii(encoding="hex"))

data = {
    "type":0,
    "fee":10000000,
    "sender":{
        "publicKey":keypair["publicKey"]
    },
    "keypair":keypair,
    "recipientId":"A79wqbYgZC5Bb923wWDXKjD7KBDn5BD6gg",
    "amount":1222222
}
_tr = tr.create(data)
print(_tr)