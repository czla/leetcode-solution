// Description:  给出两个 非空 的链表用来表示两个非负的整数。
//
//               其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
//
//               如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
//
//               您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
//
// Examples:     输入: 2 -> 4 -> 3, 5 -> 6 -> 4    输出: 7 -> 0 -> 8   原因：342 + 465 = 807
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         5/10/2019
// Performance:  40 ms, surpass 97.56%'s C++ submissions



// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode(0);
        ListNode* cur = ans;
        bool add_flag = 0;
        int x, y, temp;
        while(l1 || l2){
            if(l1){
                x = l1->val;
                l1 = l1->next;}
            else
                x = 0;
            if(l2){
                y = l2->val;
                l2 = l2->next;}
            else
                y = 0;
            temp = x + y + add_flag;
            add_flag = temp / 10;
            cur->next = new ListNode(temp % 10);
            cur = cur->next;
        }

        if(add_flag){
            cur->next = new ListNode(1);
        }

        return ans->next;
    }
};

    // use recursion
    ListNode* addTwoNumbers2(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode(0);
        ListNode* cur = ans;
        bool add_flag = 0;
        int x, y, temp;
        while(l1 && l2){
            temp = l1->val + l2->val + add_flag;
            add_flag = temp / 10;
            cur->next = new ListNode(temp % 10);
            cur = cur->next;
            l1 = l1->next;
            l2 = l2->next;
        }

        if(!l1 && !l2){
            if(add_flag)
                cur->next = new ListNode(1);
        }
        else if(!l1){
            if(add_flag)
                cur->next = addTwoNumbers(new ListNode(1), l2);
            else
                cur->next = l2;
        }
        else
            if(add_flag)
                cur->next = addTwoNumbers(new ListNode(1), l1);
            else
                cur->next = l1;

        return ans->next;
    }
};