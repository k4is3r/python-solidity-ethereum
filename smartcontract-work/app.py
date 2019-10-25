import json
from web3 import Web3

#set up connection with blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

#addres from are new contrar deploy on solidity
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
address = web3.toChecksumAddress("0xc87Bc2271031944a88F7AAdcBb509c3Bdc32caF8")

#creating a contrar value
contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.greet().call())



