class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
            Do not return anything, modify s in-place instead.
            """
        
        size = len(s)
        halfSize=int(size/2)
        last=size-1
        
        for i in range(halfSize):
            temp=s[i]
            s[i]=s[last]
            s[last]=temp
            last=last-1
