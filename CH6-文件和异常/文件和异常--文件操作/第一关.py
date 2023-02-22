import csv
def readcsv():
 #        请在此处添加代码         #
 # *************begin************#
    csv_reader = csv.reader(open("./book.csv"))
    for line in csv_reader:
        print(line[0])

 # **************end*************#



if __name__ == '__main__':
    readcsv()
