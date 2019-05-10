import hashlib

from src.base.block import Block
from src.utils.ed import Ed

block = Block()
ed = Ed()

secret = "real rally sketch sorry place parrot typical cart stone mystery age nominee"
hash = hashlib.sha256(bytes(secret, encoding="utf-8")).digest()
keypair = ed.MakeKeypair(hash)

_block = {
    'version': 0,
    'totalAmount': 0,
    'totalFee': 0,
    'reward': 600000000,
    'payloadHash': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    'timestamp': 18135589,
    'numberOfTransactions': 0,
    'payloadLength': 0,
    'previousBlock': 'b5ad296dbaa131d8d63f5569d9aa43b9fcd06d7db90e943792cdb1a10188d579',
    'generatorPublicKey': '07187396934e832fc08c8ec0f3095d6c7cce3eb2c53568f0bbafebb3ffa7c582',
    'transactions': [],
    'blockSignature': '3487e8496deae07cd6b57a1707e0becaaa0ef053198c87e02abcbb4a38a3b897942cc0924139b54aa2332598a345d33ece793e16be130d873ee1b9f2505c9608'
}

# data = {
#
# }
#
# _block = block.create(data)
# print(_block)

_blockBytes = block.getBytes(_block)
print(_blockBytes)

_blockHash = block.getHash(_block)
print(_blockHash)

_blockId = block.getId(_block)
print(_blockId)

_blockSign = block.getSignature(_block, keypair)
print(_blockSign)
