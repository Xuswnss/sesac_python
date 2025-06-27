print("* " * 30)

users = [
    {'name': 'Alice', 'age': 20, 'location': 'Jeju', 'car': 'BMW'},
    {'name': 'Bob', 'age': 25, 'location': 'Seoul', 'car': 'Hyundai'},
    {'name': 'Charlie', 'age': 22, 'location': 'Busan', 'car': 'Kia'},
    {'name': 'Diana', 'age': 27, 'location': 'Incheon', 'car': 'Mercedes'},
    {'name': 'Bob', 'age': 24, 'location': 'Daegu', 'car': 'Tesla'}
]

def find_user(name):
    for u in users:
        if u['name'] == name:
            return u  


def find_users(name):
    result = []
    for u in users:
        if u['name'] == name:
            result.append(u) 
    return result

def find_users_caseinsensitive(name):
    result = []
    for u in users:
        if u['name'].lower() == name.lower:
            result.append(u) 
    return result
        

print(find_users_caseinsensitive('bob'))   


def find_user2(name = None, age = None):
    for u in users:
        
        # if u["name"] == name & u["age"] == age: # 연산자 우선순위로 인해 오류 발생
        if u["name"] == name and u["age"] == age:
            return u
        
print(find_user2('Alice', 20))
print(find_user2('Bob',24))

def find_user3(name=None, age=None):
    result =[]
    for u in users:
        if name:
            if u['name'] == name:
                if age:
                    if u['age'] == age:
                        result.append(u)
                       
                else:
                    result.append(u)
        if age:
            if u['age'] == age:
                result.append(u)
        else:
            result.append(u)
    return result
print('*'*20)
print(find_user3('Alice', 20))
print(find_user3('Bob'))



print("*"*20)
print('개선')
def find_user3(name=None, age=None):
    result =[]
    
    for u in users:
        if name is not None and age is not None:
            if u['name'] == name and u['age'] == age:
                result.append(u)
        elif name is not None:
            if u['name'] == name :
                result.append(u)
        elif age is not None:
            if u['age'] == age:
                result.append(u)
        else: result.append(u)

    return result
    
print("* " * 30)
print(find_user3('Bob'))

