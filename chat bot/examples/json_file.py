import json
value = {

}
def savedata(x):
    with open(f"{x}.json", "w") as saveddata:
        json.dump(x, saveddata, indent = len(value))
def loaddata(x):
    with open(f"{x}.json", "r") as saveddata:
        global value
        value = json.load(saveddata)