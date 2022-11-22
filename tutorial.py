print("Hello world!")

a = 10

# if (a > 10) {
#     // ceva cod
# }
# if a > 10:
#     # linia 1
#     # linia 2
#     pass 

b = 10
c = 10.5
d = "This is a string"
e = 'This is another string'
f = """This is a multiline
string
"""
g = f"This is a new string. A = {a}"
print(g)
h = True # true in JS
i = False # false in JS

print(d.find("i"))
print(d.upper())

l1 = [1, 2, "string1", "string2", [3, 4]]
l1[0] = "string3"
print(l1)

l1.append("append")
print(l1)
l1.extend([5, 6])
print(l1)
l1.remove(2)
print(l1)

t1 = (1, 2, 3, ["string1", "string2"])
t1[0]
# t1[0] = 10
t1[3][0] = "string4"

l2 = l1 
l2[0] = "new"

d1 = {
    "name": "WebApps1",
    "year": 2022,
    "uni": "RAU",
    1: "ceva",
    2: {
        "1": {
            "1": [1, 2]
        }
    }
}
from pprint import pprint
pprint(d1)
d1[2]["1"]["1"][1] = 10
pprint(d1)


d1["name"] = "Web Apps 1"
d1["new_key"] = "something"

print(list(d1.items()))

print(d1.get(2, "Valoare default"))

# and, or, not, in
if a > 10 and b > 20: 
    print(a)
elif b < 10:
    print(b)
else:
    print(c)
    
if a is not None:
    print(a)
    
# for (const el of l1) (from JS)
print("start of for")
for el in l1:
    print(el)
    print("--")
print("end of for")

# for (let i = 0; i < l1.length; i++) (from JS)
for i in range(len(l1)):
    print(i, l1[i])
    
s = 10
while s > 0:
    print(s)
    s = s - 1