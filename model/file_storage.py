import json


class FileStorage:
    def load_model_data(self,filename):
        with open(filename, 'r') as f:
           contents = f.read()
           data = json.loads(contents)
           return data
