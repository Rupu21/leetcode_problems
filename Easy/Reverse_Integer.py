def reverse(self, x: int) -> int:
        if len((str(x))) == 1:
            return x
       
        if x < 0:
            res = f"-{str(x)[:0:-1]}"
        else:
            res = str(x)[::-1]
        res = int(res)
        
        z = 2**31
        
        if res not in range(-z, z):
            return 0
        return res
