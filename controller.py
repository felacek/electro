import json
import time
import saveread

def decode(path, body):
    res = {"code": 0, "res": "", "msg": "something went wrong", "time": time.ctime()}
    if(path == '/sendOne'):
        res["res"] = str(saveread.save(body))
        res["code"] = 1
        res["msg"] = "successfully added"
    if(path == '/count'):
        res["res"] = saveread.count()
        res["msg"] = "count successful"
        res["code"] = 1
    if(path == '/readOne'):
        res["res"] = saveread.read()
        res["msg"] = "read successful"
        res["code"] = 1
    if(path == '/readSpecific'):
        ret = saveread.readspec(body)
        if (ret):
            res["res"] = ret
            res["code"] = 1
            res["msg"] = "read successful"
        else:
            res["code"] = 0
            res["msg"] = "does not exist"
    if(path == '/readAll'):
        res["res"] = saveread.readall()
        res["code"] = 1
        res["msg"] = "read successful"
        
    return json.dumps(res)
