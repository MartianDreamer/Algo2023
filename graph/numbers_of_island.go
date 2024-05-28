package graph

func NumIslands(grid [][]byte) int {
	row := len(grid)
	col := len(grid[0])
	count := 0
	visitted := make([][]bool, row)
	for i := range visitted {
		visitted[i] = make([]bool, col)
	}
	for ir, r := range grid {
		for ic, c := range r {
			if c != 49 {
				continue
			}
			if visitted[ir][ic] {
				continue
			}
			count++
			dfs(ic, ir, row, col, visitted, grid)
		}
	}
	return count
}

func neighbors(islandX int, islandY int, row int, col int, graph [][]byte) [][2]int {
	rs := make([][2]int, 0, 4)
	left := islandX - 1
	right := islandX + 1
	upper := islandY - 1
	lower := islandY + 1
	if left >= 0 && graph[islandY][left] == 49 {
		rs = append(rs, [2]int{left, islandY})
	}
	if right < col && graph[islandY][right] == 49 {
		rs = append(rs, [2]int{right, islandY})
	}
	if upper >= 0 && graph[upper][islandX] == 49 {
		rs = append(rs, [2]int{islandX, upper})
	}
	if lower < row && graph[lower][islandX] == 49 {
		rs = append(rs, [2]int{islandX, lower})
	}
	return rs
}

func dfs(islandX int, islandY int, row int, col int, visitted [][]bool, graph [][]byte) {
	if visitted[islandY][islandX] {
		return
	}
	visitted[islandY][islandX] = true
	neighbors := neighbors(islandX, islandY, row, col, graph)
	for _, v := range neighbors {
		if visitted[v[1]][v[0]] {
			continue
		}
		dfs(v[0], v[1], row, col, visitted, graph)
	}
}
