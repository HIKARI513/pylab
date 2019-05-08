#!/usr/bin/env python
"""
 Created by howie.hu at 2019/5/8.
 基于链表实现的栈
"""


class Node:
    """
    链表结构的节点
    """

    def __init__(self, data: int, next=None):
        """
        初始化Node节点
        :param data: 存储的数据
        :param next: 后继指针
        """
        self.data = data
        self.next = next


class LinkedStack:
    """
    先进后出，后进先出
    """

    def __init__(self):
        self._top: Node = None

    def push(self, value: int):
        """进栈"""
        new_top = Node(data=value)
        new_top.next = self._top
        self._top = new_top

    def pop(self):
        """链表的第一个数据就是即将出栈的"""
        if self._top:
            value = self._top.data
            self._top = self._top.next
            return value

    def __repr__(self) -> str:
        current = self._top
        nums = []
        while current:
            nums.append(current.data)
            current = current.next
        return " ".join(f"{num}]" for num in nums)


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
