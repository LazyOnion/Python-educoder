import csv
from copy import deepcopy
def readcsv():
 #        请在此处添加代码         #
 # *************begin************#
    # csv_reader = csv.reader(open("./book.csv"))
    # fl = False
    # ls = []
    # for line in csv_reader:
    #     if fl == False:
    #         fl = True
    #         a = str(line[0])
    #         b = str(line[1])
    #         dic = {a: None, b: None}
    #         continue
    #     dic = deepcopy(dic)
    #     dic[a] = line[0]
    #     dic[b] = line[1]
    #     ls.append(dic)
    # print(ls)
    reader = csv.DictReader(open("./book.csv"))
    ls = []
    for i in reader:
        ls.append(dict(i))
    print(ls)

 # **************end*************#



if __name__ == '__main__':
    readcsv()
