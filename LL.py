class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


  def deleteDuplicates(self, head):

    values = set()
    prev = None
    curr = head

    while(curr):
      if curr.val not in values:
        values.add(curr.val)
      else:
        prev.next = curr.next
        curr = prev
              
      prev = curr
      curr = prev.next

      return head
