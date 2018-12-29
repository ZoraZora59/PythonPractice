# work2.py
import re
def readfile(fname):#读文件
    try:
        f=open(fname, "r")
        ls=f.read()
        f.close()
        return ls
    except FileNotFoundError:
        print("readfile error")
        exit()

def txtformat(ls):# 格式化
    ls=ls.lower()# 统一小写
    ls = re.sub(r'[^A-Za-z]', ' ', ls)
    ls=ls.split(" ")
    while True:
        try:
            ls.remove('')
        except ValueError:
            break
    return ls

def gettxt(fname):# 封装:读文件与格式化
    return txtformat(readfile(fname))

def writetop(pos,t1,t2):# 写文件
    f=open("output.txt","w")
    stream=[str(all),' ',str(t1),' ',str(t2),'\n']
    f.writelines(stream)
    f.close()

def checkout(t1,t2):# 查全文不同
    for i in range(len(t1)):
        if(t1[i]!=t2[i]):
            print(i+1,t1[i],t2[i])

if __name__ == '__main__':
    # 文件读取
    fname="input_1.txt"
    txt1=gettxt(fname)
    fname="input_2.txt"
    txt2=gettxt(fname)
    checkout(txt1,txt2)
    exit()
