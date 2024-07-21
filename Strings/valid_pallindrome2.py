class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while (i<j):
            if s[i]!=s[j] :
                a,b=s[:i]+s[i+1:],s[:j]+s[j+1:]
                return a==a[::-1] or b==b[::-1]               
            i+=1
            j-=1

        return True
                    
