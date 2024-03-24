class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        tcache = {}
        scache = {}
        need = 0
        have = 0
        result = ""

        for c in t:
            tcache[c] = tcache.get(c, 0) + 1
            need = len(tcache.keys())
        
        

        for right in range(len(s)):
            if tcache.get(s[right]):
                cr = s[right]
                scache[cr] = scache.get(cr, 0) + 1
                
                if scache[cr] == tcache[cr]:
                    have += 1
            
            while have == need:
                # print(f"have - {have}, need - {need}")
                new_result = s[left:right+1]
                # print(f"new result - {new_result}, old result - {result}")
                if result:
                    result = new_result if len(new_result) < len(result) else result
                else:
                    result = new_result
                
                # print(f"updated result - {result}")
                
                if scache.get(s[left], 0) >= 1:
                    scache[s[left]] -= 1

                    if scache[s[left]] < tcache[s[left]]:
                        have -= 1
                left += 1
                # print(f"updated have - {have}, updated left - {left}")
        
        return result
                
                


            






    # def minWindow(self, s: str, t: str) -> str:
    #     result = ""

    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             sub_arr = s[i:j+1]
    #             contains = True
    #             csub = sub_arr
    #             print(f"sub_arr is - {sub_arr}")

    #             for c in t:
    #                 print(f"current chat in t - {c}")
    #                 if c in csub:
    #                     print(f"csub arr before modification - {csub}")
    #                     csub = csub.replace(c, '')
    #                     print(f"current char in t - {c}, sub_arr modified is - {csub}")
    #                 else:
    #                     contains=False
                
    #             if contains:
    #                 print(f"sub_arr - {sub_arr} contais t - {t} ")
    #                 bresult = result
    #                 if result:
    #                     result = sub_arr if len(sub_arr) < len(result) else result
    #                 else:
    #                     result = sub_arr
    #                 print(f"result, before - {bresult}. after - {result}")
        
    #     return result
            


        