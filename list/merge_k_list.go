package list

func MergeKLists(lists []*ListNode) *ListNode {
    var rs *ListNode= nil
	for _,l := range lists {
		rs = MergeTwoLists(rs, l)
	}
	return rs
}
