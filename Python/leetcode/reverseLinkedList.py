# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

from typing import Optional


class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    p1, p2, = None, None
    while head != None:
      p1 = head
      head = head.next
      p1.next = p2
      p2 = p1
    return p1

