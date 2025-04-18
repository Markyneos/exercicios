from typing import Optional

#Definition for a singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    ultimateHead = ListNode()
    pointer = ultimateHead
    while list1 and list2:
      if list1.val > list2.val:
        pointer.next = list2
        list2 = list2.next
      else:
        pointer.next = list1
        list1 = list1.next
      pointer = pointer.next
    if list1:
      pointer.next = list1
    else:
      pointer.next = list2
    return ultimateHead.next





