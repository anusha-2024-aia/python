print("CREATING A DICTIONARY:")
dict={
    "name":"john",
    "age":30,
    "city":"New York"
}
print(dict)

print("\n")
print("Accessing items in a dictionary:")
print("Name:",dict["name"])
print("Age:",dict["age"])
print("City:",dict["city"])

print("\n")
print("Adding items for dictionary:")
dict["job"]="Engineer"
print("Updated Dictionary:",dict)

print("\n")
print("Looping through a dictionary:")
for key, value in dict.items():
    print(key,":", value)

print("\n")
a={1,2,3}
b={3,4,5}
print(a|b)
print(a&b)
print(a-b)

