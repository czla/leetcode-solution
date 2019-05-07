// Description:  给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
//
//               说明：给定的 n 保证是有效的。
//
// Examples:     输入: 1->2->3->4->5, n = 2
//               输出: 1->2->3->5
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         5/7/2019
// Performance:  12 ms, surpass 96.50%'s C++ submissions


// Definition for singly-linked list.
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* target = head;
        ListNode* end = head;
        while(n > 0){
            if(end->next != NULL){
                end = end->next;
                n--;
            }
            else{
                head = head->next;
                return head;
            }
        }

        while(end->next != NULL){
            target = target->next;
            end = end->next;
        }
        target->next = target->next->next;

        return head;
    }
};