# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        store = []
        ans1 = float('inf')
        last, position = head.val, 2
        head = head.next
        while head and head.next:
            cur, next_val = head.val, head.next.val
            if (last > cur < next_val) or (last < cur > next_val):
                store.append(position)
            position += 1
            last = cur
            head = head.next
            n = len(store)
            if n > 1:
                ans1 = min(ans1, store[n-1] - store[n-2])
        if ans1 == float('inf'):
            return [-1, -1]
        return [ans1, store[-1] - store[0]]
