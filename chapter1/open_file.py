import os
dir_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(dir_path, 'test.txt')
try:
    file = open(file_path, 'r')
    print(file.read())
finally:
    if file:
        file.close()
with open(file_path, 'r') as f:
    print(f.read())
try:
    file = open(file_path, 'r')
    print(len(file.readlines()))
    for line in file.readlines():
        print(line)

finally:
    if file:
        file.close()
print(os.getcwd())
print(os.path.basename(__file__))
