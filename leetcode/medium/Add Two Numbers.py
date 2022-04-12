# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1 = []
        x2 = []

        while l1:
            x1.append(l1.val)
            l1 = l1.next

        while l2:
            x2.append(l2.val)
            l2 = l2.next

        num1 = int("".join(map(str, x1))[::-1])
        num2 = int("".join(map(str, x2))[::-1])
        print("".join(map(str, x1))[::-1])
        print("".join(map(str, x2))[::-1])
        print(f"answer = {num1+num2}")
        answer = ListNode()
        prev = ListNode()
        for n in str((num1 + num2))[::-1]:
            answer.val = int(n)
            answer.next = ListNode(val=int(n))
            prev = answer

        print("==" * 10)
        while answer:
            # x1.append(l1.val)
            print(answer.val)
            answer = answer.next

        return num1 + num2


s = Solution()


l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))

a = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8)))

assert s.addTwoNumbers(l1, l2) == a
