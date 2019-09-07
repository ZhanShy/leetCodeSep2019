# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            x=head.val
            vals.append(x)
            head=head.next
        size=len(vals)
        last=size-1
        for i in range(size):
            if vals[i]!=vals[last]:
                return False
            last=last-1
        return True
