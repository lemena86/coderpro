class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        answer = head = Node(0)
        remainder = 0
        while l1 or l2:
            val = l1.val + l2.val + remainder
            remainder = val // 10
            answer.val = val % 10
            if l1.next or l2.next:
                answer.next = Node(0)
                if not l1.next:
                    l1.next = Node(0)
                if not l2.next:
                    l2.next = Node(0)
            else:
                if remainder:
                    answer.next = Node(remainder)
            l1 = l1.next
            l2 = l2.next
            answer = answer.next
        return head

l1 = Node(2)
l1.next = Node(6)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)
l2.next.next.next = Node(5)

answer = Solution().addTwoNumbers(l1, l2)
while answer:
    print(answer.val)
    answer = answer.next