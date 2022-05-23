f=open("longest lettr.txt","r")
a=f.read().split()
i=0
max=a[i]
while i<len(a):
    if len(a[i])>len(max):
        max=a[i]
    i+=1
print(max)
f.close()


# user=input("enter the name")
# file=open(user)
# a=file.read()
# b=a.split()
# print(b)
# max=b[0]
# i=0
# while i<len(b):
#     if len(b[i])>len(max):
#         max=b[i]
#     i=i+1
# print("longest word is :",max)


# def getSize(fileobject):
#     fileobject.seek(0,2) # move the cursor to the end of the file
#     size = fileobject.tell()
#     return size

# file = open('jai.txt', 'rb')
# print (getSize(file))









    















