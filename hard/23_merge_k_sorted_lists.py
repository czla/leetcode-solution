# Description:  合并 k 个排序链表，返回合并后的排序链表。
#
#
# Examples:     输入：[
#                   1->4->5,
#                   1->3->4,
#                   2->6
#                 ]
#
#               输出：1->1->2->3->4->4->5->6
#
# Difficulty:   Hard
# Author:       zlchen
# Date:         5/17/2019
# Performance:  overtime


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
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

    def mergeKLists(self, lists):
        length = len(lists)
        if length > 0:
            ans = lists[0]
        else:
            return None
        for i in range(1, length):
            ans = self.mergeTwoLists(ans, lists[i])
        return ans