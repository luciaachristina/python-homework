import os
path = 'c:\\users\\lucia\\desktop'
files = []
dirs = os.listdir(path)
for file in dirs:
   print(file, 'file')
for dir in dirs:
    print(dir, 'directory')