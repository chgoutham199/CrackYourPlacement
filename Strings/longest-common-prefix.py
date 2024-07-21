class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        s=sorted(strs)
        f=s[0]
        l=s[-1]
        for i in range(min(len(f),len(l))):
            if l[i]!=f[i]:
                return ans
            ans+=l[i]
        return ans