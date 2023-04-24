code = '''
def greeting(name):
  print(f'Hello, {name}')'''
with open('mymodule.py', 'w') as f:
  f.write(code)
import mymodule
mymodule.greeting(input('Name : '))