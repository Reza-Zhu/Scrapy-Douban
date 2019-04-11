import jieba
import wordcloud
def Count(txt,str1,str2,str3):
    txt=open('%s'%txt,'rb').read()
    words=jieba.lcut(txt)
    count1=count2=count3=0
    for word in words:
        if word=='%s'%str1:
            count1=count1+1
        elif word=='%s'%str2:
            count2=count2+1
        elif word=='%s'%str3:
            count3=count3+1
    print('\'%s\'出现%d次'%(str1,count1))
    print('\'%s\'出现%d次'%(str2,count2))
    print('\'%s\'出现%d次'%(str3,count3))

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='gbk').readlines()]
    return stopwords

def movestopwords(sentence):
    stopwords = stopwordslist('stopwords.txt')
    out = ''
    for word in sentence:
        if word not in stopwords[0]:
            if word != '\t'and'\n':
                out += word
    return out

def output():
        txt = open('C:\Python\Douban\Douban\comment.txt',encoding='utf-8').read()
        res=movestopwords(txt)
        w = wordcloud.WordCloud(width=1000, font_path='C:\Windows\Fonts\msyh.ttf', height=700)
        w.generate(" ".join(jieba.lcut(res)))
        w.to_file("wordcloud.png")
        Count('C:\Python\Douban\Douban\comment.txt', '的', '也', '太')

output()