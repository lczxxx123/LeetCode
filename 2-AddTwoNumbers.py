# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
一开始慢是没注意到要求的返回值也是ListNode，返回了一个List
b.next = b = ListNode(t%10)这种写法第一次学到

T tusizi ：
I found this Stack Overflow to find out the answer.

n.next = n = ListNode(val) means first n.next = ListNode(val) then n point to the same address

n = n.next = ListNode(val) means first n = ListNode(val) , now the n is ListNode(val), then n.next point to the address ListNode(val) which means point to itself!!!
Hope this will help.

由于python的实现机制，和c++会不一样。
since for a = b = c, one way (python, for example) equivalent to

tmp = evaluate(c)
evaluate(a) = tmp
evaluate(b) = tmp

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
            
                    
                
        
