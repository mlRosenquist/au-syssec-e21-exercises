#!/usr/bin/env python3

import random
import sys
import time
from Crypto.Cipher import AES


def decrypt(seed):

    random.seed(seed)
    key = random.randbytes(16)
    with open("ciphertext.bin", 'rb') as f_in:
        data = f_in.read()

    nonce = data[:16]
    tag = data[16:32]
    aes = AES.new(key, AES.MODE_GCM, nonce=nonce)
    try:
      plainText = aes.decrypt_and_verify(data[32:], tag)
      with open("ciphertext.txt", 'wb') as f_out:
         f_out.write(plainText)# len(data) bytes
      return plainText
    finally:
        return ""





if __name__ == '__main__':
    #1632088800 -> 1632175200
    #1632127063
#    if len(sys.argv) != 3:
#        print(f'usage: {sys.argv[0]} <src-file> <dst-file>', file=sys.stderr)
#        exit(1)

    for x in range(1632088800, 1632175200):
        plainText = decrypt(x)
        if(plainText != ""):
            print(plainText)
