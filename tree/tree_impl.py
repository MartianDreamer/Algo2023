
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def make_tree(cls, nums: list[int]):
        nodes = [TreeNode(num) if num is not None else None for num in nums]
        if len(nodes) == 0:
            return None
        current_flr = [nodes.pop(0)]
        rs = current_flr[0]
        while len(current_flr) != 0:
            cur = current_flr.pop(0)
            if cur is None:
                continue
            if len(nodes) > 0:
                cur.left = nodes.pop(0)
                current_flr.append(cur.left)
            else:
                break
            if len(nodes) > 0:
                cur.right = nodes.pop(0)
                current_flr.append(cur.right)
            else:
                break
        return rs
    
    def __str__(self) -> str:
        if self.left is None and self.right is None:
            return str(self.val)
        return f"{self.val} [L: {self.left.__str__()} | R: {self.right.__str__()}]"
