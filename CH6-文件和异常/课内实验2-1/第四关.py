import json
import copy
def main(name):
 #        请在此处添加代码         #
 # *************begin************#
 with open(name, 'r') as fp:
   a = fp.readlines()
   a_1, a_2 = a[0].split()
   dic = {str(a_1): None, str(a_2): None}
   lis = []
   for z in a[1:]:
      i, j = z.split()
      dic = copy.deepcopy(dic)
      dic[str(a_1)] = i 
      dic[str(a_2)] = j
      lis.append(dic)
   print(lis)
 # **************end*************#
        
if __name__ == '__main__':
    name = input()
    main(name)
