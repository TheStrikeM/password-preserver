from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

from colorama import Fore


class RSACipher:
    def __init__(self, private_file_name, public_file_name):
        self.private_file_name = private_file_name
        self.public_file_name = public_file_name

    def encrypt(self, message: str):
        try:
            print(Fore.CYAN + "| Start encrypting...")
            byteMessage = message.encode()
            public_key = RSA.import_key(open(self.public_file_name).read())
            cipher_rsa = PKCS1_OAEP.new(public_key)
            encrypted_message = cipher_rsa.encrypt(byteMessage)
            print(Fore.CYAN + f"| Encrypting {message} success completed")
            return base64.b64encode(encrypted_message).decode()
        except Exception as e:
            raise Exception(f"Encrypt error in {e}")

    def decrypt(self, message):
        try:
            print(Fore.CYAN + "| Start decrypting...")
            decodedMessage = base64.b64decode(message)
            private_key = RSA.import_key(open(self.private_file_name).read())
            cipher_rsa = PKCS1_OAEP.new(private_key)
            decrypted_message = cipher_rsa.decrypt(decodedMessage)
            return decrypted_message.decode()
        except Exception as e:
            raise Exception(f"Decrypt error in {e}")

