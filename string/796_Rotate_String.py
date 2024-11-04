class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        goal_arr = [c for c in goal]
        for i in range(len(goal_arr)):
            goal_arr.append(goal_arr.pop(0))
            if "".join(goal_arr) == s:
                return True
        return False
 