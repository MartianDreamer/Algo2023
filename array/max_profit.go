package array

func MaxProfit(prices []int) int {
	buy_at, profit := 10_000, 0
    for _,v := range prices {
		if v < buy_at {
			buy_at = v
		}
		if v - buy_at > profit {
			profit = v - buy_at
		}
	}
	return profit
}