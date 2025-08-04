#pip install bcrypt
import bcrypt

def generate_hash(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)

hashed_pw1 = generate_hash('hello123')
hashed_pw2 = generate_hash('hello123')

print('bcrypt HASH1:' , hashed_pw1)
print('bcrypt HASH2:' , hashed_pw2)


#검증은 어떻게 해야되는 걸까?? 
# salt를 가져와서 검증을 해야 함.
# bcryp내부 함수에 checkpw()이 있음 그걸로 slat검증

print('bcrypt HASH1 암호검증:' , verify_password('hello123', hashed_pw1))
print('bcrypt HASH2 암호검증:' , verify_password('hello123', hashed_pw2))


