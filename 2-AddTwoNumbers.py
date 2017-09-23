# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
一开始慢是没注意到要求的返回值也是ListNode，返回了一个List
b.next = b = ListNode(t%10)这种写法第一次学到
"""

class Solution(object):
   
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t = 0;
        a = b = ListNode(0);
        while (l1 or l2):
            if (l1):
                t = t + l1.val
                l1 = l1.next
            if (l2):
                t = t + l2.val
                l2 = l2.next    
            b.next = b = ListNode(t%10)
            t = t / 10
            
        if (t != 0):
            b.next = b = ListNode(t)
        return a.next
            
                    
                
        