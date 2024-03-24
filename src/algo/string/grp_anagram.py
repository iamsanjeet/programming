class Solution:
    # Complexity - O(m*n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            char_arr = [0] * 26

            for ch in s:
                char_arr[ord(ch) - ord('a')] += 1
            
            if result.get(tuple(char_arr)) is not None:
               result.get(tuple(char_arr)).append(s) 
            else:
                result[tuple(char_arr)] = [s]
        
        return result.values()

    # Complexity - O(m*nlogn)
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     anagram_grp = {}

    #     for s in strs:
    #         hsh = ''.join(sorted(s))

    #         if anagram_grp.get(hsh) is not None:
    #             anagram_grp.get(hsh).append(s)
    #         else:
    #             anagram_grp[hsh] = [s]
        
    #     return anagram_grp.values()

            
        