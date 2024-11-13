struct ListNode
{
    int val;
    struct ListNode *next;
};


struct ListNode *partition(struct ListNode *head, int x)
{
    struct ListNode *prev_pivot = 0;
    struct ListNode *pivot = head;
    if (head == 0)
    {
        return head;
    }
    while (pivot != 0 && pivot->val < x)
    {
        prev_pivot = pivot;
        pivot = pivot->next;
    }
    struct ListNode *prev = pivot;
    while (prev != 0 && prev->next != 0)
    {
        struct ListNode *cur = prev->next;
        if (cur->val < x)
        {
            prev->next = cur->next;
            cur->next = pivot;
            if (prev_pivot == 0)
            {
                head = cur;
            }
            else
            {
                prev_pivot->next = cur;
            }
            prev_pivot = cur;
            continue;
        }
        prev = prev->next;
    }
    return head;
}
