def genP1Rect(x, y, w, h):
    '''
       根据x,y,w,h值，输出图像文件表示
       :x是图像的宽
       :y是图像的高
       :w是白色块的宽
       :h是白色快的高
       :return: 图像文件的表示
    '''
    string = ''
    print("P1",end="\n")
    print(x,y)
    for i in range(y):
        for j in range(x):
            if i >= 1 and i <= h and j >= 1 and j <= w:
                string = string+'1 '
            elif j != x - 1:
                string = string + '0 '
            else:
                string = string + '0'
        string = string + '\n'
    return string
