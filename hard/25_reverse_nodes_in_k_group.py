# Description:  给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
#               k 是一个正整数，它的值小于或等于链表的长度。
#
#               如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#
# Examples:     输入: 1->2->3->4->5 k=2
#               输出: 2->1->4->3->5
#               输入: 1->2->3->4->5 k=3
#               输出: 3->2->1->4->5
#
# Difficulty:   Hard
# Author:       zlchen
# Date:         7/24/2019
# Performance:  76 ms, surpass 57.04%'s python3 submissions


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        start = head
        cnt = k - 1
        if k == 1 or not head:
            return head

        # if length < k, return
        while start.next and cnt:
            start = start.next
            cnt -= 1
        if cnt:
            return head

        # get first k value
        end = start.next
        start.next = None

        # print first k value
        # while head:
        #     print(head.val)
        #     head = head.next

        # reverse first k value
        res = self.reverse(head)
        res_end = res

        # get the end of reversed k value
        while res_end.next:
            res_end = res_end.next

        # recursion
        res_end.next = self.reverseKGroup(end, k)

        return res

    # reverse a list
    def reverse(self, head: ListNode):
        if not head or not head.next:
            return head
        temp = head.next
        res = self.reverse(head.next)
        temp.next = head
        head.next = None

        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    # nums = [12]
    head = ListNode(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next

    # while head:
    #     print(head.val)
    #     head = head.next

    # ans = Solution().reverse(head)
    ans = Solution().reverseKGroup(head, 3)
    while ans:
        print(ans.val)
        ans = ans.next