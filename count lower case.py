lower_case=0
f=open("islower.txt","r")
line=f.read()
for i in line:
    if (i.islower()==True):
        lower_case+=1
print("total no. of lower case",lower_case)

upper_case=0
f=open("isupper.txt","r")
line=f.read()
for i in line:
    if (i.isupper()==True):
       upper_case+=1
print("total no. of upper case",upper_case)

