
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {

    public List<Double> averageOfLevels(TreeNode root) {
        Queue<TreeNode> border = new LinkedList<>(); // set up breadth first search
        List<Double> rs = new LinkedList<>(); // result
        border.offer(root);
        rs.add(root.val / 1.0);
        double total = 0;
        int levelCount = 1; // all nodes in border are from a new level
        while (!border.isEmpty()) { // doing bread first search after discover all nodes on a level, calculate average and add into result

            if (levelCount == 0) {
                levelCount = border.size();
                rs.add(total / levelCount);
                total = 0;
            }
            TreeNode frontier = border.poll();
            levelCount--;
            if (frontier.left != null) {
                border.offer(frontier.left);
                total += frontier.left.val;
            }
            if (frontier.right != null) {
                border.offer(frontier.right);
                total += frontier.right.val;
            }

        }
        return rs;
    }
}

class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
