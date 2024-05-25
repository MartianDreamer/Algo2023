package list

type ListNode struct {
	Val  int
	Next *ListNode
}

func MakeList(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}
	rs := &ListNode{Val: nums[0], Next: nil}
	head := rs
	for _,v := range nums[1:] {
		head.Next = &ListNode{Val: v, Next: nil}
		head = head.Next
	}
	return rs
}