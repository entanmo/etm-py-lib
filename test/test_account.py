from src.base.account import Account

account = Account()

secret = "real rally sketch sorry place parrot typical cart stone mystery age nominee"
keypair = account.getKeypairBySecret(secret)
print(keypair)

addr = account.getAddressByPublicKey(keypair["publicKey"])
print(addr)