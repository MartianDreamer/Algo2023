package array

func ContainsDuplicate(nums []int) bool {
	int_map := make(map[int]bool, len(nums))
	for _, num := range nums {
		if _, ok := int_map[num]; ok {
			return true
		}
		int_map[num] = true
	}
	return false
}
