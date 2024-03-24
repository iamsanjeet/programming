class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        lst = []
        mapper = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            # print(f"current char is - {char}")
            if char in ['(', '[', '{']:
                # print("It is an open bracket")
                # print(f"list before append - {lst}")
                lst.append(char)
                # print(f"list after append - {lst}")
            elif len(lst) == 0:
                return False
            else:
                # print(f"Last characted in list - {lst[-1]}")
                if char == mapper.get(lst[-1]):
                    # print(f"lst before pop is - {lst}")
                    ele = lst.pop()
                    # print(f"Popped character is - {ele}")
                    # print(f"lst after pop is - {lst}")
                else:
                    return False
        
        return len(lst) == 0

        