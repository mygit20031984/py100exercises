import json

with open("company1.json", "r+") as file:
    d = json.loads(file.read())
    d["employees"].append({"firstName": "A2", "lastName": "K2"})
    file.seek(0)
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()
