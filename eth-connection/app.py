from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/dcd2563341014d5aac03472df4c67ad7"

web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.isConnected() :
    print("You r connected to ethereum blockchain")
else:
    print("Something is not working.... dont get the connection")

print("Last block in ethereum-chain")
print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0xCA558C1CD9E99241C06da63aD46CfBEAC8FEB1Af")

print("My account balance")
print(web3.fromWei(balance, "ether"))

#Normal code to get good programing things
if __name__ == "__main__":
    pass