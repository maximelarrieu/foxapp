person = {
    "name": "John",
    "age": 20,
}

print(person)
print(person['name'])

person['age'] = 44
print(person)

person['gender'] = 'male'
print(person)

print(person.keys())
print(person.values())