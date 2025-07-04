
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        temp = ListNode()
        firstRound = True


        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                if firstRound:
                    temp.val = list1.val
                    ans = temp
                    firstRound = False
                else:
                    temp.next = list1
                    temp = temp.next
                list1 = list1.next
            else:
                if firstRound:
                    temp.val = list2.val
                    ans = temp
                    firstRound = False
                else:
                    temp.next = list2
                    temp = temp.next
                list2 = list2.next
        

        while (list1 is not None):
            if firstRound:
                temp.val = list1.val
                ans = temp
                firstRound = False
            else:
                temp.next = list1
                temp = temp.next
            list1 = list1.next

        while (list2 is not None):
            if firstRound:
                temp.val = list2.val
                ans = temp
                firstRound = False
            else:
                temp.next = list2
                temp = temp.next
            list2 = list2.next
        

        return ans