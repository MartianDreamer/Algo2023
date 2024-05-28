package binary

func MissingNumber(nums []int) int {
	total := len(nums) * (len(nums) - 1) / 2
	for _, e:= range nums {
		total -= e
	}
	return total
}