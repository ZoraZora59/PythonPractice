# work1.py
def readfile(fname):#读文件并初始化输出文件
    try:
        f=open(fname, "r")
        ls=f.read()
        f.close()
        f=open("output.txt","w")
        f.close()
        return ls
    except all:
        print("readfile error")
        exit()

def txtformat(ls):# 格式化
    ls=ls.lower()
    ls=ls.replace("—"," ")
    ls=ls.replace(".\n","")
    ls=ls.replace(".","")
    ls=ls.replace(",","")
    ls=ls.split(" ")
    return ls

def gettxt(fname):# 封装:读文件与格式化
    return txtformat(readfile(fname))

def getagg(ls):# 获取集合
    agg=set(ls)
    # print(agg1)
    return agg

def writefile(fname,ls):# 写入文件
    f=open(fname,"a")
    # TODO : f.writelines or f.write
    f.writelines(ls)
    f.write('\n')
    f.close()

def countsame(s,cmp):# 查两字符串相同词的数量
    count=0;
    for item in s:
        if(item in cmp):
            count+=1
    return count

def countdiff(nall,nsame):# 查不同单词数，nall总数-nsame相同单词数=不同单词数
    return nall-nsame

if __name__ == '__main__':
    fname="input_1.txt"
    txt1=gettxt(fname)
    fname="input_2.txt"
    txt2=gettxt(fname)
    agg1=getagg(txt1)
    agg2=getagg(txt2)
    ct=50000
    print("same word =", countsame(agg1,agg2))
    # print(txt1)
