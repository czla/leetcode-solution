// Description:  给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
//
//               k 是一个正整数，它的值小于或等于链表的长度。
//
//               如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
//
//
// Examples:     输入: 1->2->3->4->5 k=2
//               输出: 2->1->4->3->5
//               输入: 1->2->3->4->5 k=3
//               输出: 3->2->1->4->5
//
// Difficulty:   Hard
// Author:       zlchen
// Date:         7/24/2019
// Performance:  28 ms, surpass 87.27%'s C++ submissions

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


class Solution {
public:
    // reverse a list
    ListNode* reverse(ListNode* head) {
        if(!head || !head->next)
            return head;
        ListNode* temp = head->next;
        ListNode* res = reverse(head->next);
        temp->next = head;
        head->next = NULL;

        return res;
    }


    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* start = head;
        int cnt = k - 1;
        if(k == 1 || !head)
            return head;

        // if length < k, return
        while(start->next && cnt){
            start = start->next;
            cnt--;
        }
        if(cnt)
            return head;

        // get first k value
        ListNode* end = start->next;
        start->next = NULL;

        // reverse first k value
        ListNode* res = reverse(head);
        ListNode* res_end = res;

        // get the end of reversed k value
        while(res_end->next)
            res_end = res_end->next;

        // recursion
        res_end->next = reverseKGroup(end, k);

        return res;
    }


};