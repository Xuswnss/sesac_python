import mymodule
from mymodule import greet as gt

print(gt('sesac'))

greeting = mymodule.greet('xuswns')
print(greeting)

print(mymodule.goodbye())

print(mymodule.default_name)