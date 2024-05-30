from node import Node


class Solution(object):
    def cloneGraph(self, node: Node):
        return self.cloneGraphRecur(node, dict())

    def cloneGraphRecur(self, node, remDict):
        if node is None:
            return None
        if node in remDict:
            return remDict[node]
        noneList = [None] * len(node.neighbors)
        cloneNode = Node(node.val, noneList)
        remDict[node] = cloneNode
        for i in range(len(node.neighbors)):
            cloneNode.neighbors[i] = self.cloneGraphRecur(node.neighbors[i], remDict)
        return cloneNode
