class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1  # base case
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            
            # check how many ways we can form target
            count = prefix[curr_sum - targetSum]
            
            # add current sum to map
            prefix[curr_sum] += 1
            
            # explore children
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # backtrack
            prefix[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)