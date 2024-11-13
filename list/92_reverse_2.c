#include "list.h"
#include <stdlib.h>
#include <stdlib.h>

struct ListNode *reverseBetween(struct ListNode *head, int left, int right)
{
    if (left == right)
        return head;

    int leng = right - left + 1 + 2;
    struct ListNode **nodes = malloc(sizeof(struct ListNode *) * leng);
    nodes[0] = 0;
    struct ListNode *cur = head;
    for (int i = 1; i <= right + 1; i++)
    {
        if (i >= left - 1)
        {
            nodes[i - left + 1] = cur;
        }
        if (cur != 0)
        {
            cur = cur->next;
        }
    }
    for (int i = 1; i <= (1 + leng - 2) / 2; i++)
    {
        struct ListNode *t = nodes[i];
        nodes[i] = nodes[leng - 1 - i];
        nodes[leng - 1 - i] = t;
        if (nodes[i - 1] != 0)
        {
            nodes[i - 1]->next = nodes[i];
        }
        nodes[i]->next = nodes[i + 1];
        nodes[leng - 1 - i - 1]->next = nodes[leng - 1 - i];
        nodes[leng - 1 - i]->next = nodes[leng - 1 - i + 1];
    }
    head = nodes[0] == 0 ? nodes[1] : head;
    free(nodes);
    return head;
}
