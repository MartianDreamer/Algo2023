
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def make_tree(cls, nums: list[int | None]):
        nodes = [TreeNode(n) if n is not None else None for n in nums]
        for i in range(len(nodes)//2):
            if nodes[i] is None:
                continue
            nodes[i].left, nodes[i].right = nodes[i * 2 + 1], nodes[i * 2 + 2] # type: ignore
        return nodes[0] if len(nodes) > 0 else None
    