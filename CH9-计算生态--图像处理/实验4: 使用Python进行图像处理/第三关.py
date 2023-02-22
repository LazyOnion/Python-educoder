import cv2
import numpy as np

thresholdBlack = 120 # RGB 都小于这个值、或者灰度图像的值小于这个值，认为是 黑色
thresholdWhite = 200 # RGB 都大于这个值、或者灰度图像的值大于这个值，认为是 白色

def fnJudge(fnIn, fnOut):
    numBlack = 0 # 记录 黑子 数目
    numWhite = 0 # 记录 白子 数目

    # Begin-end之间，补充读入文件、转换为灰度图的代码
    #********** Begin *********#
    imgIn = cv2.imread(fnIn, 3)
    gray_img = cv2.cvtColor(imgIn, cv2.COLOR_BGR2GRAY)
    #********** End **********#


    circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, minDist=80,
    param1=100, param2=35, minRadius=20, maxRadius=110)

    circles = np.uint16(np.around(circles))
    # Begin-end之间，补充显示，计算的代码
    #********** Begin *********#
    for idx, i in enumerate(circles[0,:]): # 请思考，为啥用 [0, :]    
        # 画圆的轮廓，注意 i[0] 是画图时的x坐标，i[2] 是圆的半径
        # 使用的颜色是 BGR = (0,255,0)，也就是纯绿色。注意OpenCV的颜色顺序，是BGR
        if gray_img[i[1]][i[0]] < thresholdBlack:
            numBlack += 1
        if gray_img[i[1]][i[0]] > thresholdWhite:
            numWhite += 1
        cv2.circle(imgIn,(i[0],i[1]), i[2],(0,255,0), 2) 
        # 在圆心处用红色画一个小圆
        cv2.circle(imgIn,(i[0],i[1]), 2, (0,0,255), 3)
        # 在圆心处，写上这是找到的第几个圆
        cv2.putText(imgIn, '%s' %(idx), (i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), thickness=2)
        cv2.waitKey()
        cv2.imwrite(fnOut, imgIn)
    #********** End **********#

    return (numBlack, numWhite)
