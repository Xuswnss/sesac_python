from flask import Flask, jsonify

app = Flask(__name__)


users = [
    {'name' : 'Alice', 'age': 22, 'mobile' : '010-1234-1234'},
    {'name' : 'Bob', 'age': 23, 'mobile' : '010-4321-1234'},
    {'name' : 'Charlie', 'age': 24, 'mobile' : '010-1234-4321'},
    {'name' : 'Xuswns', 'age': 25, 'mobile' : '010-1111-1234'},
    
]

@app.route('/')
def index():
    return jsonify(users)

# 검색
@app.route('/user/<name>')
def get_user_by_name(name):
  #대소문자
  print(type(name))
  name = name.upper()
  print('이름 : ' ,name)
  user = "Not found"
  for u in users:
      if name == u['name'].upper():
          print('매치')
          user = u
          break
  if user:
        return jsonify(user)
  else:
        return jsonify({'error' : 'User not found'}), 404
          


# 검색
@app.route('/user/<int:age>')
def get_user_by_age(age):
  print(type(age))
  age = int(age)
  user = None
  for u in users:
    if age == u['age']:
        user = u
        print(user)
        break              
  if user:
        return jsonify(user)
  else:
        return jsonify({'error' : 'User not found'}), 404
 
if __name__ == '__main__':
    app.run(debug=True, port=5050)