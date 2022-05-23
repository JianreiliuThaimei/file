def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

file = open('file_size.txt', 'rb')
print (getSize(file))