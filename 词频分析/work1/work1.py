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
    except FileNotFoundError:
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

def sortdict(dic):# 键值表排序
    items=dic.items()
    sd=[[v[1],v[0]] for v in items]
    sd.sort(reverse=True)
    return [ sd[i][1] for i in range(0,len(sd))]

def countdic(t1,t2):# 生成字典
    count_dict = dict()
    for item in t1:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    for item in t2:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

def gettxt(fname):# 封装:读文件与格式化
    return txtformat(readfile(fname))

def getagg(ls):# 获取集合
    agg=set(ls)
    # print(agg1)
    return agg

def writetop(all,t1,t2):# 写文件表头
    f=open("output.txt","a")
    stream=[str(all),'\n',str(t1),'\n',str(t2),]
    f.writelines(stream)
    f.close()

def countsame(s,cmp):# 查两字符串相同词的数量
    count=0
    for item in s:
        if(item in cmp):
            count+=1
    return count

def countdiff(nall,nsame):# 封装：查不同单词数
    return nall-nsame

def countall(txt):# 封装：查总词数
    return len(txt)

def typeout(sd,d):# 输出高频词表
    f=open("output.txt","a")
    for i in range(10):
        print(sd[i],d.get(sd[i]))
        stream=['\n',str(sd[i]),' ',str(d.get(sd[i]))]
        f.writelines(stream)
    while True:
        try:
            if(d.get(sd[i])==d.get(sd[i+1])):
                i+=1
                print(sd[i],d.get(sd[i]))
                stream=['\n',str(sd[i]),' ',str(d.get(sd[i]))]
                f.writelines(stream)
            else:
                f.close()
                break
        except IndexError:
            f.close()
            break
    print("=========================")

if __name__ == '__main__':
    # 文件读取
    fname="input_1.txt"
    txt1=gettxt(fname)
    fname="input_2.txt"
    txt2=gettxt(fname)
    # 去重
    agg1=getagg(txt1)
    agg2=getagg(txt2)
    # 统计词量
    same=countsame(agg1,agg2)
    a1=countall(agg1)
    a2=countall(agg2)
    print("same word =", same)
    a1=countdiff(a1,same)
    print("non-repeating word in text1 =",a1)
    a2=countdiff(a2,same)
    print("non-repeating word in text2 =",a2)
    writetop(same,a1,a2)
    # 高频统计排序
    dic=countdic(txt1,txt2)
    sortdic=sortdict(dic)
    typeout(sortdic,dic)
    exit()
