# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        a=[]
        for listnode in lists:
            c=listnode
            while c:
                a.append(c.val)
                c=c.next
        
        a.sort()
        head= ListNode(-1)
        c=head
      
        for x in a:
            c.next=ListNode(x)
            
            c=c.next
        # print(head)
        head=head.next
        # print(head)
        return head