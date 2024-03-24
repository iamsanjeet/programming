class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if not self.isAlphaNum(s[start]):
                start += 1
                continue
            
            if not self.isAlphaNum(s[end]):
                end -= 1
                continue
            
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True

    
    def isAlphaNum(self, char):
        # print(f"isAlphaNum - {char}")
        return (ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'))
    # def isPalindrome(self, s: str) -> bool:
    #     new_s = ""

    #     for char in s:
    #         if char.isalnum():
    #             new_s += char.lower() if char.isalpha() else char
        
    #     print(f"New string is - {new_s}")


    #     start = 0
    #     end = len(new_s) -1

    #     while start < end:
    #         if new_s[start] != new_s[end]:
    #             return False
            
    #         start += 1
    #         end -= 1
        
    #     return True