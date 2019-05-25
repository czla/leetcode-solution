// Description:  给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
//
//               你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
//
//
// Examples:     输入: 1->2->3->4
//               输出: 2->1->4->3
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         5/25/2019
// Performance:  12 ms, surpass 49.16%'s C++ submissions


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* ans = new ListNode(0);
        ListNode* cur = ans;
        while(head){
            if(head && head->next){
                cur->next = new ListNode(head->next->val);
                cur = cur->next;
                cur->next = new ListNode(head->val);
                head = head->next->next;
            }
            else{
                cur->next = new ListNode(head->val);
                head = head->next;
            }
            cur = cur->next;
        }

        return ans->next;
    }
};