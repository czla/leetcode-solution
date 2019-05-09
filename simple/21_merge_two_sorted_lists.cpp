// Description:  将两个有序链表合并为一个新的有序链表并返回。
//               新链表是通过拼接给定的两个链表的所有节点组成的。
//
// Examples:     输入: 1->2->4, 1->3->4    输出: 1->1->2->3->4->4
//
// Difficulty:   Simple
// Author:       zlchen
// Date:         5/9/2019
// Performance:  16 ms, surpass 96.96%'s C++ submissions


// Definition for singly-linked list.
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode(0);
        ListNode* cur = ans;
        while(l1 && l2){
            if(l1->val <= l2->val){
                cur->next = l1;
                l1 = l1->next;
            }
            else{
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
            if(!l1)
                cur->next = l2;
            else
                cur->next = l1;
        return ans->next;
    }
};