class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #initial version
        self.x = x
        if self.x >= 0:
            y = x ** 0.5
            return y
        #version 1: result > x
        l, r = 0, x
        while(l < r):
            mid = (l + r + 1) / 2
            result = mid * mid
            if(result > x):
                r = mid - 1
            else:
                l = mid
        return l
        #T(n) = n    