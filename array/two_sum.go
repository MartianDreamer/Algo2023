package array

func TwoSum(nums []int, target int) []int {
	meet_map := make(map[int]int)
	for k, v := range nums {
		if otherK, ok := meet_map[target-v]; ok {
			return []int{otherK, k}
		}
		meet_map[v] = k
	}
	return []int{}
}
