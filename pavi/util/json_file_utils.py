""" File to handle the operations with the JSON file """

import os
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
            detections = []
        )
        self.datetime = datetime.now().__str__()
        self.processing = algorithm

    def addObject(self, objects, frame, fps):
        if objects:
            self.fps = fps
            seconds = frame/fps
            self.processing.get("detections").append(dict(frame = frame, objects = objects, seconds = seconds))

    

    def writeObjectJsonFile(self):
        path = r"static/files"
        if not os.path.exists(path):
            os.makedirs(path)
        with open("static/files/data.json", "w") as jsonFile:
            json.dump(self.__dict__, jsonFile, indent = 2)
    