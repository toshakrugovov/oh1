from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, address_contract

w3= Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware,layer=0)

contract = w3.eth.contract(address=address_contract, abi=abi)

print(f"Баланс пользователя 1: {w3.eth.get_balance('0xAcf9D89da1e5aeB7b6e3e275bB8Ee6E8b9c074aa')}")
print(f"Баланс пользователя 2: {w3.eth.get_balance('0xae3d617fB065CFA0af7DA0B49A7F87626Bd2A094')}")
print(f"Баланс пользователя 3: {w3.eth.get_balance('0x2a006E7A392F69177084c3e93922884f704b4DD9')}")
print(f"Баланс пользователя 4: {w3.eth.get_balance('0x92499Cb557DE55eEf5b3A11f423d12EA1F2639D6')}")
print(f"Баланс пользователя 5: {w3.eth.get_balance('0x8642C6C1f30c503a8aB5f0e25a6D9CFD2f887cee')}")