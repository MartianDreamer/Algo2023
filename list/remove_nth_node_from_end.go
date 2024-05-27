package list

func RemoveNthFromEnd(head *ListNode, n int) *ListNode {
	count, point := 1, head
	var preSavedPoint *ListNode
	for point != nil {
		if count > n {
			if preSavedPoint == nil {
				preSavedPoint = head
			} else {
				preSavedPoint = preSavedPoint.Next
			}
		}
		count++
		point = point.Next
	}
	if preSavedPoint == nil {
		return head.Next
	} else if preSavedPoint.Next != nil {
		preSavedPoint.Next = preSavedPoint.Next.Next
	} else {
		preSavedPoint.Next = nil
	}
	return head
}