class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n==0:
                return 1.0
            half= pow(x,n//2)
            if n%2==1:
                return half*half*x
            else:
                return half*half
        if n<0:
            x= 1/x
            n= -n
        return pow(x,n)