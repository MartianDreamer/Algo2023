package array

func ProductExceptSelf(nums []int) []int {
	results, allProduct, zeroCount := make([]int, len(nums)), 1, 0
	var zeroPos int;
	for i, num := range nums {
		if num == 0 {
			zeroCount += 1
			zeroPos = i
		} else {
			allProduct *= num
		}
	}
	if zeroCount > 0 && zeroCount < 2 {
		results[zeroPos] = allProduct
	} else if zeroCount == 0 {
		for i:=0; i < len(results); i++ {
			results[i] = allProduct/ nums[i] 
		}
	}
	return results
}