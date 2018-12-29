# work1.py
rd=open("input_1.txt","r")
ls=rd.read()
rd.close()
# 格式化
ls=ls.lower()
ls=ls.replace(".\n","")
ls=ls.replace(".","")
ls=ls.replace(",","")
ls=ls.split(" ")
print(ls)
'''word=[]
target=open("testTarget.txt","w")
target.write('\n'.join(word))
target.close()'''
