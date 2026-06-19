# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        curr = head
        while curr != None and curr.val > count:
            count = curr.val
            curr = curr.next
        if curr != None:
            count = curr.val
            curr = curr.next
        while curr != None and curr.val > count:
            count = curr.val
            curr = curr.next
        if curr == None:
            return False
        return True