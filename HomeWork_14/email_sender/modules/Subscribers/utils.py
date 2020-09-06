import json

def loadSubscribers():
    fp = open("./data/Subscribers.json","r")
    return json.load(fp)
