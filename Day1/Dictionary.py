
#keys should not be duplicate but allows duplicate values

# Approach 1
# Dic1 = {
#     "name": "Raghu",
#     "age": 30,
#     "married": "Yes",
#     "gen": "Male"
# }
#
# print(Dic1["name"])
# print(Dic1["age"])


# Approach 2

# dic2 = dict(a="term", b=2, c="stranger")
#
# print(dic2)


# A key can contain many values
dic1 = {
"name": ["Raghu","lakshmi"],
   "age": [30,28],
    "married": ["Yes", ]

 }

print(dic1)
print(dic1["name"])
print(dic1.keys())
print(dic1.values())
print(dic1.items())

















