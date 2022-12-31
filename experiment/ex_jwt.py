import jwt

encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
print(encoded_jwt)

data = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
print(data)
