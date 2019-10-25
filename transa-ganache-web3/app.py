from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

#account to connect
account_1="0x55bc4420e2CE6fFc45dE28Eff48C3e143B5D3fCa"
account_2="0x56bF64dD3a0465E811215C174389507BA6E5da3a"

private_key_1 ="a910d1226fecb5defcfd90f9d6c75fc7123b1be131068572e0e9c41e0370eca7"

#get the nance
nonce = web3.eth.getTransactionCount(account_1)

#build transaction
tx ={
    'nonce':nonce,
    'to':account_2,
    'value':web3.toWei(3,'ether'),
    'gas':2000000,
    'gasPrice':web3.toWei('50', 'gwei')
}

# sign the transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key_1)

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

#get transaction hash
