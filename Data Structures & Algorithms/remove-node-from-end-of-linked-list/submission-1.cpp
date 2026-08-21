class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *counterPointer = head;
        int counter = 1;

        while (counterPointer->next != NULL) {
            counterPointer = counterPointer->next;
            counter += 1;
        }

        if (counter == n)
            return head->next;

        ListNode *ptr = head;

        for (int i = 0; i < (counter - n - 1); i++)
            ptr = ptr->next;

        ptr->next = ptr->next->next;
        return head;
    }
};