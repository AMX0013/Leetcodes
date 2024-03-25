/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// void print(ListNode* head) {
//     ListNode* current = head;
//     while (current != nullptr) {
//         std::cout << current->val;
//         if (current->next != nullptr) {
//             std::cout << " -> ";
//         }
//         current = current->next;
//     }
//     std::cout << std::endl;
// }


class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* current = head->next;
        while (current->next != nullptr) {
            if (current->next->val == 0) {

                if (current->next->next == nullptr){
                    current->next= nullptr;
                    return head->next;
                }

                current = current->next;
            }

            if (current->next != nullptr){
                current->val += current->next->val;
                current->next = current->next->next;
            }
        }


        // print(head);
        return head->next;
        
    }
};