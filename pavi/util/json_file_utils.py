""" File to handle the operations with the JSON file """

import json
from datetime import datetime

"""
def writeObjectJsonFile(objects):
    if len(objects) != 0:
        with open("file.json", "a") as jsonFile:
            json.dump(objects, jsonFile, indent = 4)
            jsonFile.write(",")"""

class JsonFileObject:
    
    def __init__(self):
        algorithm = dict(
            algorithm='YOLOv4',
            detections=[]
        )
        self.fps = 30
        self.datetime = datetime.now().__str__()
        self.processing = algorithm

    def addObject(self, objects):
        self.processing.get("detections").append(objects)

    def writeObjectJsonFile(self):
        with open("file.json", "w") as jsonFile:
            json.dump(self.__dict__, jsonFile, indent = 4)
        