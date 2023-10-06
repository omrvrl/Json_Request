import json


person_str = '{"name" : "Ali" , "languages" : ["python","C#"] }'
person_dic ={
    "name": "Ali",
    "languages": ["Python","C#"]
}

#Json string to Dict

# result = json.loads(person_str)
# print(type(result) )
# print(result["name"])


# with open("person.json") as f:
#     data = json.load(f)
#     print(data["languages"])



# result = json.dumps(person_dic)            #dictionary to json string
# print(result)

# with open("person.json","w") as f:
#     json.dump(person_dic,f)

# with open("person.json","w") as w:
#     json.dump(person_dic,w)

# person_dic = json.loads(person_str)
# result = json.dumps(person_dic,indent=2,sort_keys=True)
# print(result)



# print(person_dic)
# print(type(person_dic))

# print(person_str)
# print(type(person_str))

person_str = json.dumps(person_dic)
person_dic = json.loads(person_str)
with open("person.json","w") as w:
    json.dump(person_str,w)

with open("person.json") as f:
    data = json.load(f)
    print(data)



