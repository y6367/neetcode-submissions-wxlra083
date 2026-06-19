# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        curr1 = list1
        curr2 = list2
        result = ListNode(-101)
        result_curr = result
        while curr1 != None and curr2 != None:
            temp = ListNode()
            if curr1.val < curr2.val:
                temp = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                temp = ListNode(curr2.val)
                curr2 = curr2.next

            if result.val == -101:
                result = temp
                result_curr = result
            else:
                result_curr.next = temp
                result_curr = result_curr.next
                
        if curr1 != None:
            if result.val == -101:
                result = curr1
            else:
                result_curr.next = curr1
        if curr2 != None:
            if result.val == -101:
                result = curr2
            else:
                result_curr.next = curr2
        return result
        