package binary

func CountBits(n int) []int {
	rs := make([]int, n+1)
	for i := range n + 1 {
		count := 0
		for num := i; num != 0; num >>= 1 {
			if num&1 == 1 {
				count += 1
			}
		}
		rs[i] = count
	}
	return rs
}