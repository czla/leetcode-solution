# Description:  给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
#               你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
# Examples:     输入: 1->2->3->4
#               输出: 2->1->4->3
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/25/2019
# Performance:  56 ms, surpass 54.96%'s python3 submissions


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ans = ListNode(0)
        cur = ans
        while head:
            if head and head.next:
                cur.next = ListNode(head.next.val)
                cur = cur.next
                cur.next = ListNode(head.val)
                head = head.next.next
            else:
                cur.next = ListNode(head.val)
                head = head.next

            cur = cur.next
        return ans.next

if __name__ == '__main__':
    nums = [1, 2, 4]
    # nums = [1, 2]
    head = ListNode(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next

    # while head:
    #     print(head.val)
    #     head = head.next

    ans = Solution().swapPairs(head)
    while ans:
        print(ans.val)
        ans = ans.next