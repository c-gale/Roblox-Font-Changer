import json
from os import path

def readJsonFile(path:str) -> dict:
    """Returns a dict of a json file given it's file path"""
    try:
        tmpFile = open(path, "r")
        jsonData = json.load(tmpFile)
        tmpFile.close()
        return jsonData
    except Exception as e:
        print(f"Error reading json: {e} ")

