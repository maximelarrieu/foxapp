# If / Elif / Else
print("------IF ELIF ELSE------")

count = 15

if count < 10:
    print('count is less than 10:', count)
elif count == 10:
    print('count is 10')
else:
    print('count is greater than 10: {}'.format(count))

notify_user = True if count > 10 else False

name = "Doe"

if name != "John":
    print("Hello stranger!")
elif not name:
    print("Empty name :(")


languages = ["Javascript", "Python"]

if "Python" in languages:
    print('Python not exists!')


# For
print("------FOR------")
languages = ["Javascript", "Python", "Ruby", "C"]

for language in languages:
    if language == "Javascript":
        continue
    elif language == "C":
        break
    print(language)

words = {
    "Hello": "You say yes",
    "Goodbye": "You say no",
}

for word, sentence in words.items():
    print(word + " => " + sentence)

total = 0
for i in range(1, 10):
    total = total + 1

print(total)
total = 0
for i in range(20, 0, -10):
    total += 1
print(total)


# While
password = ""
canceled = False
while password != "root":
    print("Secret password?")
    password = input()

    if password == "exit":
        canceled = True
        break

if canceled:
    print("Don't give up")
else:
    print("You found the secret password")