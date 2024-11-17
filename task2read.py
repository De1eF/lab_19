import shelve

with shelve.open("db.db") as db:
    keyList = db['countries']
    valueList = db['populations']

res = {}
for key in keyList:
    for value in valueList:
        res[key] = value
        valueList.remove(value)
        break

print("Reading:")
print(res)
