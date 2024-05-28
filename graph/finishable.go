package graph

func CanFinish(numCourses int, prerequisites [][]int) bool {
	graph := make([][]int, numCourses)
	for _, pre := range prerequisites {
		if v := graph[pre[0]]; v != nil {
			graph[pre[0]] = append(graph[pre[0]], pre[1])
		} else {
			graph[pre[0]] = make([]int, 1, numCourses)
			graph[pre[0]][0] = pre[1]
		}
	}
	visitted := make([]int, numCourses)
	for i := range numCourses {
		if dfs_cycle_detect(i, graph, visitted) {
			return false
		}
	}
	return true
}

// 0 not visit, 2 being visitting, 1 not cycle, 3 cycle
func dfs_cycle_detect(root int, graph [][]int, status []int) bool {
	if status[root] == 2 {
		status[root] = 3
		return true
	} else if status[root] != 0 {
		return status[root] == 3
	}
	status[root] = 2
	for _, v := range graph[root] {
		if dfs_cycle_detect(v, graph, status) {
			status[root] = 3
			return true
		}
	}
	status[root] = 1
	return false
}

func Bfs_detect_cycle(root int, numCourses int, graph [][]int) bool {
	queue := make([]int, 0, numCourses)
	queue = append(queue, root)
	visitted := make([]bool, numCourses)
	for len(queue) > 0 {
		s := queue[0]
		visitted[s] = true
		queue = queue[1:]
		for _, v := range graph[s] {
			if !visitted[v] {
				queue = append(queue, v)
			} else if v == root {
				return true
			}
		}
	}
	return false
}
