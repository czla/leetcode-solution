// Description:  合并 k 个排序链表，返回合并后的排序链表。
//
//
// Examples:     输入：[
//                   1->4->5,
//                   1->3->4,
//                   2->6
//                 ]
//
//               输出：1->1->2->3->4->4->5->6
//
// Difficulty:   Hard
// Author:       zlchen
// Date:         5/17/2019
// Performance:  208 ms, surpass 26.98%'s C++ submissions



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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int length = lists.size();
        ListNode* ans;
        if (length)
            ans = lists[0];
        else
            return 0;

        for(int i = 1; i != length; ++i){
            ans = mergeTwoLists(ans, lists[i]);
        }
        return ans;
    }
};