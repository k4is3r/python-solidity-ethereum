import json
from web3 import Web3

#set up connection with blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

#checking the connection
if web3.isConnected():
    print('Welcome to the blockchain network. you are connected to ganache')
else:
    print('Something going wrong, check ganache instance')

#signed account 
web3.eth.defaultAccount = web3.eth.accounts[0]

#addres from are new contrar deploy on solidity
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
address = web3.toChecksumAddress("0xc87Bc2271031944a88F7AAdcBb509c3Bdc32caF8")

#creating a contrar value
contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('New greeting').transact()

web3.eth.waitForTransactionReceipt(tx_hash)
print('Updated greeting: {}'.format(
    contract.functions.greet().call()
))

#print(web3.toHeh(tx_hash))

