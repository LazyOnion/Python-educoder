
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置

        :param x: 新的横坐标
        "param y: 新的纵坐标
        :return : 无返回值
        """
        #        请在此处添加代码       #
        # *************begin************#
        self.x = x
        self.y = y
        return 
        # **************end*************#

    def move_by(self, dx, dy):
        """移动指定的增量

        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        :return : 无返回值
        """
        #        请在此处添加代码       #
        # *************begin************#
        self.x = self.x + dx
        self.y = self.y + dy
        return 
        # **************end*************#

    def distance_to(self, other):
        """计算与另一个点的距离

        :param other: 另一个点,坐标为(other.x,other.y)
        ：return ：返回两点之间的距离
        """
        #        请在此处添加代码       #
        # *************begin************#
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5
        # **************end*************#

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


