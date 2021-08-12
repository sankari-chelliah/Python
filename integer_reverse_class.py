class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        from math import copysign
        sign = lambda m : copysign(1, m)

        self.x=x
        s=sign(x)
        y = abs(x)
        z=str(y)
        a=z[::-1]
        b=int(a)
        
        if (b & 0x7fffffff) == b:
             if s<0:
                return(-b)
             else:
                return(b)
        else:
            return(0)
