from nacl.public import PrivateKey, PublicKey, Box
from nacl.encoding import HexEncoder

private_key = PrivateKey.generate()
public_key = private_key.public_key

box = Box(private_key, public_key)

message = b'Dit is een test bericht'

encrypted_message = box.encrypt(message)

print("Encrypted boodschap:", encrypted_message.ciphertext.hex())
print("Private keys:", private_key.encode(encoder=HexEncoder).decode())
print("Public key:", public_key.encode(encoder=HexEncoder).decode())
