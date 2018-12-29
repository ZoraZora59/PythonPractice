# work2.py
# work1.py
import re
def readfile(fname):#读文件并初始化输出文件
    try:
        f=open(fname, "r")
        ls=f.read()
        f.close()
        f=open("output.txt","w")
        f.close()
        return ls
    except :
        print("readfile error")
        exit()

def txtformat(ls):# 格式化
    ls=ls.lower()
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

def writetop(all,t1,t2):# 写文件表头
    f=open("output.txt","a")
    stream=[str(all),'\n',str(t1),'\n',str(t2),]
    f.writelines(stream)
    f.close()

def countall(txt):# 封装：查总词数
    return len(txt)

if __name__ == '__main__':
    # 文件读取
    fname="input_1.txt"
    txt1=gettxt(fname)
    fname="input_2.txt"
    txt2=gettxt(fname)
