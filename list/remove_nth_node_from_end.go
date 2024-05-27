package list

func RemoveNthFromEnd(head *ListNode, n int) *ListNode {
	count, point := 1, head
	var preRemovedPoint *ListNode
	for point != nil {
		if count > n {
			if preRemovedPoint == nil {
				preRemovedPoint = head
			} else {
				preRemovedPoint = preRemovedPoint.Next
			}
		}
		count++
		point = point.Next
	}
	if preRemovedPoint == nil {
		return head.Next
	} else if preRemovedPoint.Next != nil {
		preRemovedPoint.Next = preRemovedPoint.Next.Next
	} else {
		preRemovedPoint.Next = nil
	}
	return head
}