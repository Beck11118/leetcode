from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head
        print(head)
            if head is None or head.next == None:
            return head
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid.next)
        return self.merge(left, right)
    

    def get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next

            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left or right # Add remaining nodes
        return dummy.next # We need to skip dummy node


        

def test():
    sol = Solution()
    ListNode(4,2,3,1)
    test_case = (
        ListNode([4,2,1,3]),
    )
    for h in test_case:
        print(sol.sortList(h))
             
test()