# -*- encoding: utf-8 -*-


import hashlib
from binascii import hexlify, unhexlify

from src.base.transaction import Transaction
from src.utils.ed import Ed

tr = Transaction()
ed = Ed()


def createTrs(data):
    hash = hashlib.sha256(bytes(data["secret"], encoding="utf-8")).digest()
    # print(hexlify(hash))

    keypair = ed.MakeKeypair(hash)
    # print(keypair['publicKey'].to_ascii(encoding="hex"))
    # print(keypair['privateKey'].to_ascii(encoding="hex"))

    data["sender"] = {
        "publicKey": keypair["publicKey"]
    }
    data["keypair"] = keypair

    _tr = tr.create(data)
    return _tr


data0 = {
    "secret": "laundry hockey oppose void announce stay transfer prefer syrup review lottery great",
    "type": 0,
    "fee": 10000000,
    "recipientId": "A79wqbYgZC5Bb923wWDXKjD7KBDn5BD6gg",
    "amount": 1200000000
}
# tr0 = createTrs(data0)
# print(tr0)

data1 = {
    "secret": "laundry hockey oppose void announce stay transfer prefer syrup review lottery great",
    "type": 2,
    "fee": 10000000,
    "username": "bbb"
}
# tr1 = createTrs(data1)
# print(tr1)

data2 = {
    "secret": "laundry hockey oppose void announce stay transfer prefer syrup review lottery great",
    "type": 120,
    "fee": 10000000
}
# tr2 = createTrs(data2)
# print(tr2)

data3 = {
    "secret": "worry net spend unfold desert trust dove waste grain people swap twelve",
    "type": 101,
    "fee": 10000000,
    "args": ["100000000"]
}
# tr3 = createTrs(data3)
# print(tr3)

data4 = {
    "secret": "worry net spend unfold desert trust dove waste grain people swap twelve",
    "type": 102,
    "fee": 10000000,
    "args": ["14d4cd9fd313f92ebd5bb4850204d78d86658dd88a17087f0916ca5b13ce3c13"]
}
# tr4 = createTrs(data4)
# print(tr4)

data5 = {
    "secret": "worry net spend unfold desert trust dove waste grain people swap twelve",
    "type": 3,
    "fee": 10000000,
    "votes": ["+c6b1f18afa85a21df50cf9580c63c0aca4643a4a4e4ec93c2e397c81e87879b9"]
}
# tr5 = createTrs(data5)
# print(tr5)

data6 = {
    "secret": "laundry hockey oppose void announce stay transfer prefer syrup review lottery great",
    "type": 110,
    "fee": 10000000,
    "recipientId": "A79wqbYgZC5Bb923wWDXKjD7KBDn5BD6gg",
    "amount": 1200000000,
    "args": ["1556640000000"]
}
# tr6 = createTrs(data6)
# print(tr6)

secondHash = hashlib.sha256(bytes("asd", encoding="utf-8")).digest()
secondKeypair = ed.MakeKeypair(secondHash)
data7 = {
    "secret": "laundry hockey oppose void announce stay transfer prefer syrup review lottery great",
    "type": 1,
    "fee": 10000000,
    "secondKeypair": secondKeypair
}
# tr7 = createTrs(data7)
# print(tr7)

data8 = {
    "secret": "real rally sketch sorry place parrot typical cart stone mystery age nominee",
    "type": 9,
    "fee": 10000000000,
    "name": "QQQ",
    "desc": "QQQ desc"
}
# tr8 = createTrs(data8)
# print(tr8)

data9 = {
    "secret": "real rally sketch sorry place parrot typical cart stone mystery age nominee",
    "type": 10,
    "fee": 50000000000,
    "name": "QQQ.WWW",
    "desc": "QQQ desc",
    "maximum": '1000000000000',
    "precision": 4,
    "strategy": '',
    "allowBlacklist": 0,
    "allowWhitelist": 0,
    "allowWriteoff": 0
}
# tr9 = createTrs(data9)
# print(tr9)

data13 = {
    "secret": "real rally sketch sorry place parrot typical cart stone mystery age nominee",
    "type": 13,
    "fee": 10000000,
    "currency": "QQQ.WWW",
    "amount": '1000000000000'
}
# tr13 = createTrs(data13)
# print(tr13)

data11 = {
    "secret": "real rally sketch sorry place parrot typical cart stone mystery age nominee",
    "type": 11,
    "fee": 10000000,
    "currency": "QQQ.WWW",
    "flagType": 1,
    "flag": 2
}
# tr11 = createTrs(data11)
# print(tr11)

data12 = {
    "secret": "real rally sketch sorry place parrot typical cart stone mystery age nominee",
    "type": 12,
    "fee": 10000000,
    "currency": "QQQ.WWW",
    "operator": "aaaa",
    "flag": 1,
    "list": ["a","b"]
}
# tr12 = createTrs(data12)
# print(tr12)

data14 = {
    "secret": "real rally sketch sorry place parrot typical cart stone mystery age nominee",
    "recipientId": "A79wqbYgZC5Bb923wWDXKjD7KBDn5BD6gg",
    "type": 14,
    "fee": 10000000,
    "currency": "QQQ.WWW",
    "amount": "100000000"
}
tr14 = createTrs(data14)
print(tr14)
