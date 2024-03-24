# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next

    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     size = 0
    #     tail = head

    #     while tail:
    #         size += 1
    #         tail = tail.next
    #     # print(f"size of node list - {size}")

    #     if size == 1 and n == 1:
    #         return None
        
    #     before_del_pos = size - n
    #     if before_del_pos == 0:
    #         return head.next
    #     del_pos = size - n + 1

    #     pos = 1
    #     ptr = head
    #     while pos < before_del_pos:
    #         ptr = ptr.next
    #         pos += 1

    #     if n == 1:
    #         ptr.next = None
    #     else:
    #         jump_ptr = ptr
    #         jump_ptr = jump_ptr.next.next
    #         ptr.next = jump_ptr
        
    #     return head
        


        