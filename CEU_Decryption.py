# %%

import os

from pathlib import Path

from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

PROJECT_FOLDER = os.getcwd()
print(PROJECT_FOLDER)

PRIVATE_KEY_FILE = PROJECT_FOLDER + "\keypairs\my_keypair"
print(PRIVATE_KEY_FILE)

assert os.path.isfile(PRIVATE_KEY_FILE)
# %%

# Load the private key from file
with open(PRIVATE_KEY_FILE, "r", encoding="utf8") as key_file:
    private_key = RSA.import_key(key_file.read())


# %%
ENCRYPTED_MESSAGE_FILE = PROJECT_FOLDER + "\encrypted_message.bin"
# %%
with open(ENCRYPTED_MESSAGE_FILE, "rb") as f:
    encrypted_message_from_file = f.read()

private_key_cipher = PKCS1_OAEP.new(private_key)
decrypted_message = private_key_cipher.decrypt(encrypted_message_from_file)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")
# %%
