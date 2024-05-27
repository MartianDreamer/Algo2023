package graph

import "fmt"

func CanFinish(numCourses int, prerequisites [][]int) bool {
	preMap := make([][]int, numCourses)
	for _, pre := range prerequisites {
		if v := preMap[pre[0]]; v != nil {
			preMap[pre[0]] = append(preMap[pre[0]], pre[1])
		} else {
			preMap[pre[0]] = make([]int, 1, numCourses)
			preMap[pre[0]][0] = pre[1]
		}
	}
	remMap := make([]int, numCourses)
	for i := range numCourses {
		if cycle_detect(i, preMap, remMap) {
			return false
		}
	}
	return true
}

func cycle_detect(root int, preMap [][]int, remMap []int) bool {
	if remMap[root] == -2 {
		remMap[root] = 1
		return true
	} else if remMap[root] == 1 {
		return true
	} else if remMap[root] == -1 {
		return false
	}
	remMap[root] = -2
	for i := 0; i < len(preMap[root]); i++ {
		fmt.Printf("root: %v\tnextRoot: %v\n", root, preMap[root][i])
		if cycle_detect(preMap[root][i], preMap, remMap) {
			remMap[preMap[root][i]] = 1
			remMap[root] = 1
			return true
		} else {
			remMap[preMap[root][i]] = -1
		}
	}
	remMap[root] = -1
	return false
}
