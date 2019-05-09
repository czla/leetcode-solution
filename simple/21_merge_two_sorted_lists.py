# Description:  将两个有序链表合并为一个新的有序链表并返回。
#               新链表是通过拼接给定的两个链表的所有节点组成的。
#
# Examples:     输入: 1->2->4, 1->3->4    输出: 1->1->2->3->4->4
#
# Difficulty:   Simple
# Author:       zlchen
# Date:         5/9/2019
# Performance:  60 ms, surpass 83.61%'s python3 submissions


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        cur = ans
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if not l1:
            cur.next = l2
        else:
            cur.next = l1

        return ans.next

if __name__ == '__main__':
    nums1 = [1, 2, 4]
    nums2 = [1, 3, 4]
    l1 = ListNode(nums1[0])
    start = l1
    for i in nums1[1:]:
        start.next = ListNode(i)
        start = start.next

    l2 = ListNode(nums2[0])
    start = l2
    for i in nums2[1:]:
        start.next = ListNode(i)
        start = start.next

    ans = Solution().mergeTwoLists(l1, l2)
    while ans != None:
        print(ans.val)
        ans = ans.next