class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        i=0
        j=1
        k=1
        a = 0
        
        if n<=1:
            a = n
             
        else:
            while k<n:
                a=i+j
                i=j
                j=a
                k=k+1
            
        return (a)
