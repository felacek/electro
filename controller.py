import json
import secrets

def parse(data):
    try:
        return json.loads(data.decode("utf-8"))
    except:
        return 0

def decode(path, body):
    data = parse(body)
    res = {"code": 0, "msg": "incorrect path"}
    if(path == '/sendOne'):
        res["code"] = 1
        res["msg"] = ("In left:\nVoltage: %s V\nCurrent: %s A\nIn center:\n Voltage: %s V\nCurrent: %s A\nIn center:\nVoltage: %s V\nCurrent: %s A\n\n" % (data["lu"],  data["li"], data["cu"], data["ci"], data["ru"], data["ri"]))
    return json.dumps(res)
