package binary

func ReverseBits(num uint32) uint32 {
	var total uint32 = 0
	for i := 0; i < 32; i++{
		bit := num & 1
		total = (total << 1) | bit
		num >>= 1
	}
	return total
}