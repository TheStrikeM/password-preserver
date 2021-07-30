import os
import json


class JSONAdapter:
    def __init__(self, file_name):
        self.file_name = file_name

    def _clear_json(self):
        try:
            os.remove(self.file_name)
            file = open(self.file_name, "w+")
            return file
        except Exception as e:
            raise Exception(f"Error in clear_json: ${e}")

    def write_to_json(self, _platform: str, _message: str):
        try:
            file = open("data.json", "r")
            text = file.read()

            encrypted_file = json.loads(text)
            encrypted_file[_platform] = _message
            file.close()

            file = self._clear_json()
            file.write(json.dumps(encrypted_file))
            readFile = file.read()
            return readFile
        except Exception as e:
            raise Exception(f"Error in write_to_json: ${e}")

    def delete_in_json(self, _platform: str):
        try:
            items = json.loads(open(self.file_name).read())
            del items[_platform]
            self._clear_json()
            with open(self.file_name, "w+") as newFile:
                newFile.write(json.dumps(items))
        except Exception as e:
            raise Exception(f"Error in delete_in_json: ${e}")