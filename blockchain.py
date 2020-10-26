print("Importing Blockchain")
from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.exceptions import AddressNotFound

__all__ = ["GenAddr","GetBalance"]

client = Tron()
def GenAddr():
    info = client.generate_address()
    result = [info["base58check_address"],info["private_key"]]
    return result
def GetBalance(addr):
    try:
        result = client.get_account_balance(addr)
    except AddressNotFound:
        result = False
    return result
    







"""
owner = "TPvC9qQLX4xQ8MUstqfxM3UjJR2GiJXH7E"
addr2 = "TJs8BSGZzH1dzSi9XornysKz3eoGjt61fo"

testnet_addr = "TPrKRhyYiyFNpXp3yFDk3RdxrmzcRiadE3"
testnet_addr2= "TKUmQ4BhuB1wi6MhBFWwYos1i7JVSAYMS6"

encrypted_priv_key = "bf87aabe40d4f53dbfbb4be4ae70c626b0dee2d68c8aa590e9a05cbc9f0572fb"
encrypted_priv_key2= "ad4a1775563fe697ef017cba1e34562a923929bfaab46e8b9ddf1fdeb28b5068"

private_key = PrivateKey(bytes.fromhex(encrypted_priv_key))
private_key2= PrivateKey(bytes.fromhex(encrypted_priv_key2))

client = Tron()

#system('clear')
while True:
    print("___________")
    txn = (client.trx.transfer(
        from_ = testnet_addr,
        to = testnet_addr2,
        amount = 1_000_000).memo("Testing").build().sign(private_key))
    txn.broadcast()
    print(client.get_account(testnet_addr))
    print(client.get_account(testnet_addr2))
    sleep(1)

def gen_addr_now():
    gen_addr = client.generate_address()
    print("Address:",gen_addr['base58check_address'])
    print("Private Key:",gen_addr['private_key'])
contract = client.get_contract("TDgbvGz99eqfCxcvhVhHuFiiYehPnSNKTQ")
print(contract.functions.balanceOf(owner))
"""
print("Imported Blockchain")