import csv
def readcsv():
 #        请在此处添加代码         #
 # *************begin************#
    csv_reader = csv.reader(open("./book.csv"))
    fl = False
    for line in csv_reader:
        if fl == False:
            fl = True
            continue
        print(line)

 # **************end*************#



if __name__ == '__main__':
    readcsv()
