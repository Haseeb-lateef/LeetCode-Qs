# Definition for singly-linked list.

# class ListNode:

# def **init**(self, val=0, next=None):

# self.val = val

# self.next = next

from typing import Optional


class Solution:
     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          if head is None:
               return None
          current = head
          before = None

          while current != None:
               after = current.next
               current.next = before
               before = current
               current = after

          return before


