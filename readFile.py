#Reading all contents of the file
# handle = open("test.txt",'r')

# data = handle.read()
# print(data)

# handle.close()

#Reading a single line
handle = open("test.txt","r")

data = handle.readline()
print(data)

handle.close()