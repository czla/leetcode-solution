# Description:  给出两个 非空 的链表用来表示两个非负的整数。
#
#               其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
#               如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
#               您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# Examples:     输入: 2 -> 4 -> 3, 5 -> 6 -> 4    输出: 7 -> 0 -> 8   原因：342 + 465 = 807
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/10/2019
# Performance:  104 ms, surpass 88.79%'s python3 submissions


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = ListNode(0)
        cur = ans
        add_flag = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            temp = x + y + add_flag
            add_flag = temp // 10
            cur.next = ListNode(temp % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if add_flag:
            cur.next = ListNode(1)

        return ans.next

    # method2 use recursion to solve add_flag
    def addTwoNumbers2(self, l1, l2):
        ans = ListNode(0)
        cur = ans
        add_flag = 0
        while l1 and l2:
            temp = l1.val + l2.val + add_flag
            add_flag = 0
            if temp >= 10:
                temp -= 10
                add_flag = 1
            cur.next = ListNode(temp)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        if not l1 and not l2:   # both List arrive terminal
            if add_flag:
                cur.next = ListNode(add_flag)
        elif not l1:    # l1 gets terminal
            cur.next = self.addTwoNumbers(ListNode(1), l2) if add_flag else l2
        else:           # l2 gets terminal
            cur.next = self.addTwoNumbers(ListNode(1), l1) if add_flag else l1

        return ans.next

if __name__ == '__main__':
    nums1 = [2, 6]
    nums2 = [1, 4, 9, 9]
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

    ans = Solution().addTwoNumbers(l1, l2)
    while ans != None:
        print(ans.val)
        ans = ans.next