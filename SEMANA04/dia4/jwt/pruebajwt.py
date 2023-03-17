import jwt
encoded_jwt = jwt.encode({"usuario":"cesar"},"secret",algorithm="HS256")
print(encoded_jwt)

decode_jwt = jwt.decode(encoded_jwt,"secret",algorithms=["HS256"])
print(decode_jwt)