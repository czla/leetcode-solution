# Description:  给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
#               说明：给定的 n 保证是有效的。
#
# Examples:     输入: 1->2->3->4->5, n = 2
#               输出: 1->2->3->5
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/7/2019
# Performance:  88 ms, surpass 15.52%'s python3 submissions


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n: int):
        end = head
        target = head
        while n > 0:
            if end.next != None:
                end = end.next
                n -= 1
            else:
                head = head.next
                return head
        while end.next != None:
            target = target.next
            end = end.next
        target.next = target.next.next
        return head