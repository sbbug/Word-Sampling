import numpy as np


if __name__=="__main__":
    f = open("../data/company0124.txt",encoding="utf-8")

    line = f.readline()
    words = {}#建立常用公司的字库
    all_words = []#所有单词

    while line:
        line = line.replace("\n","")

        for w in line:
            if words.get(w)==None:
                words[w]=1
            elif words.get(w)!=None:
                words[w]=words[w]+1

        line = f.readline()
    f.close()

word_n = 0 #字的总数
for key in words.keys():
    word_n=word_n+words[key]

#抽取字典中出现频率比较高的词
right_words = []
right_words_fre = []
right_n = 0

#筛选字典中频率出现比较高的词
for key in words.keys():
    if words[key]>600:
        right_n = right_n+words[key]
        right_words.append(key)

#计算符合要求的词出现的频率
for key in words.keys():
    right_words_fre.append(words[key]/right_n)

main_word_list = []
n=0

while True:
    str=''
    indexs = []

    if n==500000:
        break

    if n%3==0:
        i_s = np.random.choice(len(right_words),3,right_words_fre)
    elif n%3==1:
        i_s = np.random.choice(len(right_words),2,right_words_fre)
    elif n % 3 ==2:
        i_s = np.random.choice(len(right_words), 4, right_words_fre)

    for i in i_s:
        str+=right_words[i]

    if str not in main_word_list:
        main_word_list.append(str)
        n=n+1
        print(str)

f_r = open("../data/newMain.txt","w+",encoding="utf-8")

for ls in main_word_list:
    f_r.write(ls+"\n")

f_r.close()
