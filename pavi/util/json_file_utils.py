""" File to handle the operations with the JSON file """

import json

def writeObjectJsonFile(objects):
    with open("file.json", "a") as jsonFile:
        
        jsonFile.write(str(objects) + "\n")

"""class JsonFileObject:

    def __init__(self, dict):
        self.fps = 0"""