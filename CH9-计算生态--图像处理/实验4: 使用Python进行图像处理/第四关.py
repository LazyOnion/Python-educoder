import cv2
import numpy as np

### begin ###
import utils
### end ###

def fnJudge(fnIn, fnOut):
    #WW begin ###
    img = utils.fnPerspectiveCorrection(fnIn)  # 使用utils里面的fnPerspectiveCorrection，对fnIn 做透视矫正
    ### end ###

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转换为灰度

    circles = cv2.HoughCircles(      # 查找 圆
        imgGray, cv2.HOUGH_GRADIENT, 1, minDist=60,
        param1=80, param2=30, minRadius=5, maxRadius=500)

    circles = np.uint16(np.around(circles))

    for idx, i in enumerate(circles[0,:]):
        # 画轮廓
        cv2.circle(img,(i[0],i[1]), i[2], (255,255,255), 2)
        # 画圆心
        cv2.circle(img,(i[0],i[1]), 2, (255,255,255), 3)

        ### begin ###
        # 计算半径大小（单位：mm）
        mmperpixle = 297/imgGray.shape[0]
        radius = 2*mmperpixle*i[2]
        # 这里补全
        # 在矫正之后的图中，标注半径数值，保留到小数点后2位
        cv2.putText(img, 'r='+str(radius)+'cm', (i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), thickness=1)

        # 在矫正之后的图中，标注表示半径的箭头
        cv2.arrowedLine(img,(i[0],i[1]),(i[0],i[1]+i[2]),
                (255, 255, 255),
                thickness=3, line_type=8, shift=0, tipLength=0.2
        )

        print(radius) # 输出直径

        ### end ###

    cv2.imwrite(fnOut, img)
