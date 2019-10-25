filename = "housing.data"
file = open(filename, "r")
for line in file:
   print (line)

filename = "housing.data"
file = open(filename, "r")
for x in file:
    print(x.replace('\n','').split("  "))

