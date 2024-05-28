package graph

func NumIslands(grid [][]byte) int {
	row := len(grid)
	col := len(grid[0])
	count := 0
	for ir, r := range grid {
		for ic, c := range r {
			if c != 49 {
				continue
			}
			count++
			dfs(ic, ir, row, col, &grid)
		}
	}
	return count
}

func neighbors(islandX int, islandY int, row int, col int) [][2]int {
	rs := make([][2]int, 0, 4)
	left := islandX - 1
	right := islandX + 1
	upper := islandY - 1
	lower := islandY + 1
	if left >= 0 {
		rs = append(rs, [2]int{left, islandY})
	}
	if right < col {
		rs = append(rs, [2]int{right, islandY})
	}
	if upper >= 0 {
		rs = append(rs, [2]int{islandX, upper})
	}
	if lower < row {
		rs = append(rs, [2]int{islandX, lower})
	}
	return rs
}

func dfs(islandX int, islandY int, row int, col int, graph *[][]byte) {
	if (*graph)[islandY][islandX] != 49 {
		return
	}
	(*graph)[islandY][islandX] = 50
	neighbors := neighbors(islandX, islandY, row, col)
	for _, v := range neighbors {
		dfs(v[0], v[1], row, col, graph)
	}
}
