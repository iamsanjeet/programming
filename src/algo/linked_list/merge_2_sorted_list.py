# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     dummy = ListNode()
    #     head = dummy

    #     while True:
    #         if list1 is None and list2 is None:
    #             break
    #         if list1 is None and list2:
    #             head.next = list2
    #             break
    #         elif list2 is None and list1:
    #             head.next = list1
    #             break
    #         else:
    #             if list1.val < list2.val:
    #                 head.next = list1
    #                 list1 = list1.next
    #                 head = head.next
    #             else:
    #                 head.next = list2
    #                 list2 = list2.next
    #                 head = head.next
        
    #     return dummy.next


