class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        ran = {}
        for i in magazine:
            mag[i] = mag.get(i, 0) + 1
            
        for k in ransomNote:
            ran[k] = ran.get(k, 0) + 1
        
        for i, v in ran.items():
            if i in mag and ran[i] <= mag[i]:
                continue
            else:
                return False
        return True

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         x=Counter(ransomNote)
#         y=Counter(magazine)
#         for i,v in x.items():
#             if(x[i]<=y[i]):
#                 continue
#             else:
#                 return False
#         return True