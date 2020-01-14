""" 删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5 """


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head.next is None:
            return None
        slow = head
        fast = head.next
        while fast.next:
            if slow.next.val == val:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        return head
