package list

func HasCycle(head *ListNode) bool {
	meet_map := make(map[*ListNode]bool)
	for head != nil {
		if _, ok := meet_map[head]; ok {
			return true
		}
		meet_map[head] = true
		head = head.Next
	}
	return false
}
