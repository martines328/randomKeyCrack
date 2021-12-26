import time

import bitcoin
import requests
import _thread

print("Started search...")


def run():
    global decoded_private_key
    while True:
        valid_private_key = False
        while not valid_private_key:
            private_key = bitcoin.random_key()
            decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
            valid_private_key = 0 < decoded_private_key < bitcoin.N

        wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
        public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)

        r = requests.get("https://blockchain.info/q/getsentbyaddress/"+bitcoin.pubkey_to_address(public_key))

        if int(r.text) > 0:
            resultFile = open("result.txt", "w+")

            print("Bitcoin Address is:", str(bitcoin.pubkey_to_address(public_key)))
            print("Private Key is: ", str(wif_encoded_private_key))
            print("Balance is: ", str(r.text))
            resultFile.write(str(wif_encoded_private_key) + "  wif private key")
            resultFile.write(str(bitcoin.pubkey_to_address(public_key)) + "  address public")
            resultFile.flush()
            resultFile.flush()
            resultFile.close()


while True:
    try:
        _thread.start_new_thread(run())
        _thread.start_new_thread(run())
        _thread.start_new_thread(run())
        _thread.start_new_thread(run())
        _thread.start_new_thread(run())
        # run()

    except Exception as ex:
        print(ex)


