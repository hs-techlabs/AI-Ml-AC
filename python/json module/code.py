import json

'''json code to python code'''
# json_str='{"name":"ram","post":"god","isTrue":true}'

# py_obj=json.loads(json_str)
# print(type(py_obj),py_obj)


'''python code to json code'''
# py_obj={"name":"ram"
#         ,"post":"god",
#         "isTrue":True}

# json_str=json.dumps(py_obj)
# print(type(json_str),json_str)



'''to copy all the code from json file'''
# with open("/Users/himanshusharma/Desktop/learning/AI:ML-AC/python/json module/data.json","r") as f:
#     py_obj=json.load(f)
#     print(py_obj)
    


'''to coly all python code on json file'''
d= {
    "name": "Shradha",
    "age": 27,
    "isTeacher": True
}
with open("/Users/himanshusharma/Desktop/learning/AI:ML-AC/python/json module/data.json","w") as f:
    json.dump(d,f,indent=4, sort_keys=True)