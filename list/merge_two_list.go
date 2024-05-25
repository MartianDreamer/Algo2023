package list

func MergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	oldL1, oldL2 := list1, list2

	if list1 == nil {
		return list2
	} else if list2 == nil {
		return list1
	}

	for list1 != nil && list2 != nil {
		var prev, start, end *ListNode
		for list1 != nil && list1.Val <= list2.Val {
			prev = list1
			list1 = list1.Next
		}
		start = list2
		for list1 != nil && list2 != nil && list2.Val <= list1.Val {
			end = list2
			list2 = list2.Next
		}
		if prev != nil {
			prev.Next = start
		}
		if end != nil {
			end.Next = list1
		}
	}

	if oldL1.Val <= oldL2.Val {
		return oldL1
	} else {
		return oldL2
	}
}
