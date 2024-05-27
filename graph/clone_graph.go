package graph

func CloneGraph(node *Node) *Node {
	return cloneGraphRecur(node, make(map[*Node]*Node))
}

func cloneGraphRecur(node *Node, remMap map[*Node]*Node) *Node {
	if node == nil {
		return nil
	}
	if v,ok := remMap[node]; ok {
		return v
	}
	clonedGraph := &Node{Val: node.Val, Neighbors: make([]*Node, len(node.Neighbors))}
	remMap[node] = clonedGraph
	for i, e := range node.Neighbors {
		clonedGraph.Neighbors[i] = cloneGraphRecur(e, remMap)
	}
	return clonedGraph
}