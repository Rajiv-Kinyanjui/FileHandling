#Reading all contents of the file
with open("test.txt","r") as handle:
    data = handle.read()
    print(data)


#Reading a single line
# handle = open("test.txt","r")

# data = handle.readline()
# print(data)

# handle.close()


#Reading multiple lines
# handle = open("test.txt","r")

# data = handle.readlines()
# print(data)

# handle.close()


#Looping through the file
# handle = open("test.txt","r")

# data = handle.read()
# counter = 0
# for word in data.split():
#     if word == "Python":
#         counter += 1
# print(counter)