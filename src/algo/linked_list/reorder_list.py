# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd list
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        
        # merge
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2


    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     """
    #     Do not return anything, modify head in-place instead.
    #     """
    #     ptr = head
    #     dummy = ListNode()
    #     cursor = dummy

    #     cache = []

    #     while ptr:
    #         temp = ptr
    #         ptr = ptr.next
    #         temp.next = None
    #         cache.append(temp)
        
    #     i = 0
    #     j = len(cache) - 1

    #     while i < j:
    #         ln1 = cache[i]
    #         ln2 = cache[j]

    #         cursor.next = ln1
    #         ln1.next = ln2
    #         cursor = ln2

    #         i+=1
    #         j-=1
        
    #     if i == j:
    #         cursor.next =  cache[i]
    

    #     head = dummy.next


        
        

        