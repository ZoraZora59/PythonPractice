# work1.py
def readfile(fname):#读文件
    try:
        f=open(fname, "r")
        ls=f.read()
        f.close()
        return ls
    except all:
        print("readfile error")
        exit()

def txtformat(ls):# 格式化
    ls=ls.lower()
    ls=ls.replace(".\n","")
    ls=ls.replace(".","")
    ls=ls.replace(",","")
    ls=ls.split(" ")
    return ls

def gettxt(fname):# 封装:读文件与格式化
    return txtformat(readfile(fname))

def getagg(ls):#获取集合
    agg=set(ls)
    # print(agg1)
    return agg

def writefile(fname,txt):#写入文件
    f=open(fname,"w")
    # TODO : f.writelines or f.write
    f.write(txt)
    f.write('\n')
    f.close()

if __name__ == '__main__':
    fname="input_1.txt"
    txt1=gettxt(fname)
    fname="input_2.txt"
    txt2=gettxt(fname)
    agg1=getagg(txt1)
    
    # print(txt1)
