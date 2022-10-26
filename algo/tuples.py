result = (False, "Oops something went wrong...", 44)

print(result)

print(result[0])

# Unpack
error, message, _ = result
print(message)
