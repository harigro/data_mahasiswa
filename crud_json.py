import json



def setDataJsonFile(data: dict, fd: str):
    with open(fd, "w") as f:
	    return json.dump(data, f, indent=4)

def getDataJsonFile(fd: str) -> dict:
    with open(fd, 'r') as f:
	    return json.load(f)

