package binary

func GetSum(a int, b int) int {
	if a & b != 0 {
		return GetSum(a ^ b, a & b << 1)
	}
	return a ^ b
}