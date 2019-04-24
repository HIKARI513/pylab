#!/usr/bin/env python
"""
 Created by howie.hu at 2019/4/24.
 问题：如果字符串是通过单链表来存储的，那该如何来判断是一个回文串呢？
 思路：
    - 快慢指针定位中间节点
        - 快指针每次前进两步
        - 慢指针每次前进一步
    - 将后半部分逆序
    - 循环比较，判断是否为回文
"""

from singly_linked_list import SinglyLinkedList


def reverse(head):
    """
    反转单项链表
    :param head:
    :return:
    """
    reverse_head = None
    while head:
        next = head.next
        head.next = reverse_head
        reverse_head = head
        head = next

    return reverse_head


def is_palindrome(l: SinglyLinkedList) -> bool:
    """
    判断是否是回文字符串
    :param l:
    :return:
    """
    l.print_all()
    fast = slow = l._head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    reverse_node = reverse(slow)
    head_node = l._head
    is_palin = True
    while head_node and reverse_node:
        if head_node.data == reverse_node.data:
            head_node = head_node.next
            reverse_node = reverse_node.next
        else:
            is_palin = False
            break

    return is_palin


if __name__ == "__main__":
    # the result should be False, True, True, True, True
    test_str_arr = ["ab", "aa", "aba", "abba", "abcba"]
    for str in test_str_arr:
        l = SinglyLinkedList()
        for i in str:
            l.insert_value_to_head(i)

        print(is_palindrome(l))
