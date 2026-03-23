class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {v: i for i, v in enumerate(inorder)}
        
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            # pick root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            # split inorder
            mid = index_map[root_val]
            
            # build left first, then right
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(inorder) - 1)