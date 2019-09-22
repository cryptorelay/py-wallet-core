import walletcore

words = 'ripple scissors kick mammal hire column oak again sun offer wealth tomorrow wagon turn fatal'
passphrase = 'TREZOR'
assert walletcore.is_valid_mnemonic(words)

coin = 'Ethereum'
wallet = walletcore.HDWallet(mnemonic=words, passphrase=passphrase)
key = wallet.key_for_coin(coin)
key1 = wallet.key_for_bip44(coin)
assert key.data == key1.data, 'impossible'
addr = key.address(coin)
pub = key.public_key(walletcore.curve_type(coin), False)
addr1 = pub.address(coin)
assert addr == addr1 == '0x27Ef5cDBe01777D62438AfFeb695e33fC2335979'
