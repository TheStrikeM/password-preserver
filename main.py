import sys
import json
from colorama import Fore, Back, Style


from cipheration.RSAAdapter import RSACipher
from log.JSONAdapter import JSONAdapter

rsa_adapter = RSACipher('private.pem', 'public.pem')
json_adapter = JSONAdapter('data.json')
items = json.loads(open("data.json").read())

arg_type = str(sys.argv[1])
if arg_type == "encrypt":
    _platform = str(sys.argv[2])
    message = str(sys.argv[3])
    cipher = rsa_adapter.encrypt(message)
    json_adapter.write_to_json(_platform, cipher)

elif arg_type == "decrypt":
    _platform = str(sys.argv[2])
    message = items[_platform]
    print(Fore.CYAN + f"| Your password is: {rsa_adapter.decrypt(message)}")

elif arg_type == "list":
    print(Fore.CYAN + "| All platforms:")
    for item in items:
        print(f"| - {item}")

elif arg_type == "delete":
    _platform = str(sys.argv[2])
    json_adapter.delete_in_json(_platform)


else:
    print("Error in arg 0")
