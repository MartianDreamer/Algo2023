
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class Solution {

    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return List.of();
        }
        List<List<Integer>> rs = new LinkedList<>();
        rs.add(new ArrayList<>());
        List<TreeNode> border = new LinkedList<>();
        border.add(root);
        int bcount = 1;
        while (!border.isEmpty()) {
            if (bcount == 0) {
                bcount = border.size();
                rs.add(new ArrayList<>());
            }
            TreeNode frontier = border.removeFirst();
            bcount--;
            rs.getLast().add(frontier.val);
            if (frontier.left != null) {
                border.add(frontier.left);
            }
            if (frontier.right != null) {
                border.add(frontier.right);
            }
        }
        return rs;
    }
}
