banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("file-question3.txt","w")
i=0
while i<len(banks_list):
    if banks_list[i]:
        f.write(banks_list[i]+"\n")
    i+=1
# print(banks_list)
f.close()