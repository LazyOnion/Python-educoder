#统计一个文件中单词出现的次数，并输出出现次数最多的前3个单词
def countword(file):
    fp = open(file, mode='r')
    word_l = {}
    for line in fp:
        words = line.strip().split()
        for word in words:
            if word in word_l:
                word_l[word]+=1
            else:
                word_l[word] = 1
    word_list = sorted(word_l.items(), key=lambda e: e[1], reverse=True)
    for i,j in word_list[:3]:
        print((j,i))



file = input()
countword(file)
