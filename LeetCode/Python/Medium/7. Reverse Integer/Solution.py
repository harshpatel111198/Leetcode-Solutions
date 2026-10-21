class Solution:
    def reverse(self, x: int) -> int:
            if -x>0:
                z= ""
                y = str(abs(x))[::-1]
                for i in y:
                    if int(i) != 0 or len(z)>0:
                        z+=i
                if -int(z)<-2147483648:
                    return 0
                else:
                    return -int(z)
            elif x==0:
                return x
            else:
                y = str(x)[::-1]
                z= ""
                for i in y:
                    if int(i) != 0 or  len(z)>0:
                        z+=i 
                if int(z)>2147483647:
                    return 0
                else:
                    return int(z)
                