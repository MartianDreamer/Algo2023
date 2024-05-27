package list

func ReorderList(head *ListNode) {
	nodes := [5 * 10_000]*ListNode{}
	count := 0
	for point := head; point != nil; point = point.Next {
		nodes[count] = point
		count += 1
	}
	for i := 0; i < count/2; i++ {
		nodes[i].Next = nodes[count-1-i]
		nodes[count-1-i].Next = nodes[i+1]
	}
	nodes[count/2].Next = nil
}
