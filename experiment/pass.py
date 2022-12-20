from passlib.hash import pbkdf2_sha256
from passlib import pwd


# generate new salt, and hash a password
hash = pbkdf2_sha256.hash("toomanysecrets")
print(hash)

# verifying the password
is_ok = pbkdf2_sha256.verify("toomanysecrets", hash)
print(is_ok)

is_no_ok = pbkdf2_sha256.verify("joshua", hash)
print(is_no_ok)

# generate pass
print(pwd.genword())
print(pwd.genword(entropy=52, charset="hex"))