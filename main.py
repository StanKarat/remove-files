import os

os.chdir('/Users/stanislau.karat/Documents')

for filename in os.listdir():
    if filename.endswith('.py'):
      #  os.unlink(filename)
       print(filename)
