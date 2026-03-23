class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev
        
        # Step 1: reverse
        head = reverse(head)
        
        # Step 2: filter nodes
        max_val = head.val
        curr = head
        
        while curr and curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.val
        
        # Step 3: reverse back
        return reverse(head)