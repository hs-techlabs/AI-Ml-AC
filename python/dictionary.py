'''mutable'''
info={
    "name":"himanshu",
    "age":20,
    "study":"cse",
    3.14:"Pi"
}
# print(info)
# print(len(info))
# print(info["name"])

print(info.keys())
print(info.values())
print(info.items())
print(info.get(3.14))
print(info.get("age"))

info.update({
    "city":"delhi"
})
print(info)